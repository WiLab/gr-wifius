/* -*- c++ -*- */
/*
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "measure_phases_impl.h"
#include <volk/volk.h>

#include <algorithm>

#define PI 3.14159265359

//typedef std::vector< boost::tuple<int, int> > TupVec

namespace gr {
  namespace wifius {

    measure_phases::sptr
    measure_phases::make(float SampleRate, float CalibrationToneFrequency, int UpdatePeriod, size_t vlen)
    {
      return gnuradio::get_initial_sptr
        (new measure_phases_impl(SampleRate, CalibrationToneFrequency, UpdatePeriod, vlen));
    }

    /*
     * The private constructor
     */
    measure_phases_impl::measure_phases_impl(float SampleRate, float CalibrationToneFrequency, int UpdatePeriod, size_t vlen)
      : sync_block("measure_phases",
              gr::io_signature::make(2, -1, sizeof(float)*vlen),
              gr::io_signature::make(2, -1, sizeof(int)*vlen)),
	  d_vlen(vlen),
	  d_SampleRate(SampleRate),
    d_ToneFreq(CalibrationToneFrequency),
    d_HaveBeenDelayed(false),
    d_lastUpdate(0),
    d_UpdatePeriod(UpdatePeriod)
    {
      // Samples needed to capture peaks
      d_SamplesPerPeriod = d_SampleRate/d_ToneFreq;
      d_SamplesPerRadian = 2*PI/d_SamplesPerPeriod;
      d_SamplesPerPeriodInt = (int) d_SamplesPerPeriod;
      d_SamplesInTwoPeriods = ceil((int) d_SamplesPerPeriod*2);

      d_Delays = new int[3];
      d_Delays[0]=0;d_Delays[1]=0;d_Delays[2]=0;

    }

    /*
     * Our virtual destructor.
     */
    measure_phases_impl::~measure_phases_impl()
    {
    }

    /*
     * Support Functions
     */
    int
    measure_phases_impl::GetPeak(float *signal, int &start, int &signalLength)
    {
      // This function measures the peak of a sinusoid, returns index
      int largestIndex = 0;
      for (int index = start; index < (start+signalLength); index++) {
        if (signal[largestIndex] < signal[index]) {
          largestIndex = index;
        }
      }
      //std::cout<<"PeakValue: "<<signal[largestIndex]<<std::endl;
      return largestIndex;
    }

    TupVec
    measure_phases_impl::GetAllPeaks(gr_vector_const_void_star &input_items, int &numInputs, int &start)
    {
      // Each signal will have two peaks, since we are looking at two periods
      TupVec peakIndexes;
      int p1,p2;

      int onePeriod = ceil(d_SamplesInTwoPeriods/2);
      int startPeriodTwo = start + onePeriod;

      // Get others
      for (int input=0; input< numInputs; input++)
      {
        // Get first peak of signal
        p1 = GetPeak( (float *)input_items[input], start, onePeriod);

        // Get second peak of signal
        p2 = GetPeak( (float *)input_items[input], startPeriodTwo, onePeriod);

        // Save to vector
        peakIndexes.push_back(boost::make_tuple(p1,p2));

      }

      return peakIndexes;

    }

    int*
    measure_phases_impl::DetermineCasualOffsets(TupVec positions, int &numInputs)
    {
      // Delay signals
      // Since the system is casual and we use the first input as a reference,
      // we will make sure all delays are positive values by (if necessary)
      // delaying the reference signal

      int *NewOffsets = new int[numInputs];
      int p1,p2;

      // Get first peak only for reference
      int ref = boost::get<0>(positions[0]); NewOffsets[0] = 0;

      // Assuming input 0 is the reference
      for (int input=1; input<numInputs; input++)
      {
        // Determine closer peak
        p1 = boost::get<0>(positions[input]);
        p2 = boost::get<1>(positions[input]);

        // Set offset based on closer peak
        if (abs(ref-p1)<abs(ref-p2))
        { // p1 closer
          NewOffsets[input] = (ref-p1)%d_SamplesPerPeriodInt;
        }
        else
        { // p2 closer
          NewOffsets[input] = (ref-p2)%d_SamplesPerPeriodInt;
        }

      }

      return NewOffsets;

    }

    int*
    measure_phases_impl::UpdateDelays(gr_vector_const_void_star &input_items, int &numInputs, int &start)
    {

      TupVec peakPositions;// 2 peaks per input
      int *NewOffsets;

      // Update delays to make them casual
      if (!d_HaveBeenDelayed)
      {
        // Get all peak locations for all inputs
        peakPositions = GetAllPeaks( input_items, numInputs, start );

        // Update delays to make them casual
        NewOffsets = DetermineCasualOffsets(peakPositions, numInputs);

        d_Delays = new int[numInputs];
        d_Delays = NewOffsets; // Update history
        d_HaveBeenDelayed = true && (d_UpdatePeriod>0);
      }
      else
      {
        // Reset Update Period
        if (d_lastUpdate>d_UpdatePeriod)
        {
          d_lastUpdate = 0;
          d_HaveBeenDelayed = false;
        }
        else// Increment counter
          d_lastUpdate++;

      }
      return d_Delays;
    }

    int
    measure_phases_impl::work (int noutput_items,
      gr_vector_const_void_star &input_items,
      gr_vector_void_star &output_items)
      {

        int numInputs = input_items.size(); // # Inputs
        int nitems = noutput_items*d_vlen; // # Samples
        int frameSize = d_vlen; // Vector size

        int *NewOffsets;

        // Cycle Through each frame
        int start = 0;
        for (int vec=0; vec < noutput_items; vec++)
        {
          // Offset vector by frame
          start = vec*(d_vlen);

          // Measure new offsets and adjust accordingly
          NewOffsets = UpdateDelays(input_items, numInputs, start);

          // Send to outputs
          for (int input=0; input< numInputs; input++)
          {
            // Use same offset for all samples of frame
            int *out = (int *) output_items[input];
            for (int sample=0; sample < d_vlen; sample++)
              out[start+sample] = NewOffsets[input];
          }

        }// Next frame


        // Tell runtime system how many output items we produced.
        return noutput_items;
      }

  } /* namespace wifius */
} /* namespace gr */
