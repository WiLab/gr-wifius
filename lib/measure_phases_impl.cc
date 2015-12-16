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
              gr::io_signature::make(3, 3, sizeof(float)*vlen),
              gr::io_signature::make(3, 3, sizeof(float)*vlen)),
	d_vlen(vlen),
	d_SampleRate(SampleRate),
  d_ToneFreq(CalibrationToneFrequency),
  d_HaveBeenDelayed(false),
  d_lastUpdate(0)
  {
    // Samples needed to capture peaks
    d_SamplesPerPeriod = d_SampleRate/d_ToneFreq;
    d_SamplesPerRadian = 2*PI/d_SamplesPerPeriod;
    d_SamplesNeeded = ceil((int) d_SamplesPerPeriod);

    d_Delays = new int[3];

    d_UpdatePeriod = UpdatePeriod;

  }

    /*
     * Our virtual destructor.
     */
    measure_phases_impl::~measure_phases_impl()
    {
    }

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

    float
    measure_phases_impl::GetPhaseDiff(int &distance)
    {
      // Fix > 2pi offset
      distance = distance % d_SamplesNeeded;

      float differenceInRadians = ((float) distance) * d_SamplesPerRadian;

      // Unrwap //FIXME
      // if (distance < 0)
      //   differenceInRadians = differenceInRadians+2*PI;

      return differenceInRadians;
    }

    int*
    measure_phases_impl::DetermineCasualOffsets(int *positions, int &numInputs)
    {
      // Delay signals
      // Since the system is casual and we use the first input as a reference,
      // we will make sure all delays are positive values by (if necessary)
      // delaying the reference signal

      int *NewOffsets = new int[numInputs];

      // // Find most delayed signal
      // int mostDelayedInput = 0;
      // for (int i=0; i<numInputs; i++)
      // {
      //   if (positions[i]>positions[mostDelayedInput])
      //     mostDelayedInput = i;
      // }
      // // Adjust offsets to sync them relative to the most delayed signal
      // for (int i=0; i<numInputs; i++)
      // {
      //   if (i==mostDelayedInput)
      //   {
      //     NewOffsets[i] = 0;
      //   }
      //   else
      //   {
      //     NewOffsets[i] = positions[mostDelayedInput] - positions[i];
      //   }
      // }

      // Assume input 0 if fixed or the reference
      NewOffsets[0] = 0;
      for (int i=1; i<numInputs; i++)
      {
        NewOffsets[i] = positions[0] - positions[i];
      }

      return NewOffsets;

    }


    int
    measure_phases_impl::work (int noutput_items,
      gr_vector_const_void_star &input_items,
      gr_vector_void_star &output_items)
      {

        int numInputs = input_items.size(); // # Inputs
        int nitems = noutput_items*d_vlen; // # Samples
        int frameSize = d_vlen;

        int peakPositions[input_items.size()];
        int *NewOffsets;

        // Cycle Through each frame
        int start = 0;
        for (int vec=0; vec < noutput_items; vec++)
        {
          // Offset vector by frame
          start = vec*(d_vlen);

          // Get others
          for (int input=0; input< numInputs; input++)
          {
            // Get peak position of signal
            peakPositions[input] = GetPeak( (float *)input_items[input], start, frameSize);

            // Make sure we are only looking at a period worth of data
            if (peakPositions[input]>d_SamplesNeeded)
              peakPositions[input] = peakPositions[input] % d_SamplesNeeded;

          }

          // Update delays to make them casual
          if (!d_HaveBeenDelayed)
          {
            NewOffsets = DetermineCasualOffsets(peakPositions, numInputs);
            d_Delays = NewOffsets;
            d_HaveBeenDelayed = true &&(d_UpdatePeriod>0);
          }
          else
          {
            if (d_lastUpdate>d_UpdatePeriod)
            {
              d_lastUpdate = 0;
              d_HaveBeenDelayed = false;
            }
            else
              d_lastUpdate++;

            NewOffsets = d_Delays;
          }
          // Send to outputs
          for (int input=0; input< numInputs; input++)
          {
            // Use same offset for all samples of frame
            float *out = (float *) output_items[input];
            for (int sample=0; sample < d_vlen; sample++)
              out[start+sample] = (float) NewOffsets[input];
          }

        }// Next frame

        // Tell runtime system how many output items we produced.
        return noutput_items;
      }

  } /* namespace wifius */
} /* namespace gr */
