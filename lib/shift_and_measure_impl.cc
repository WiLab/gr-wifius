/* -*- c++ -*- */
/*
 * Copyright 2016 <+YOU OR YOUR COMPANY+>.
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
#include "shift_and_measure_impl.h"

#define dout(X,Y) {if(d_debug){std::cout<<X<<": "<<Y<<std::endl;}}

#define HIST_SIZE 0

namespace gr {
  namespace wifius {

    shift_and_measure::sptr
    shift_and_measure::make(float cal_tone_freq, float samp_rate, size_t vlen, float mu, bool debug)
    {
      return gnuradio::get_initial_sptr
        (new shift_and_measure_impl(cal_tone_freq, samp_rate, vlen, mu, debug));
    }

    /*
     * The private constructor
     */
    shift_and_measure_impl::shift_and_measure_impl(float cal_tone_freq, float samp_rate, size_t vlen, float mu, bool debug)
      : gr::sync_block("shift_and_measure",
              gr::io_signature::make(2, 2, vlen*sizeof(float)),
              gr::io_signature::make(1, 1, sizeof(int))),
	  d_vlen(vlen),
    d_lastDelay(0),
    d_mu(mu),
    d_debug(debug)
    {
      float samplesPerPeriod = (int) ceil( (samp_rate/cal_tone_freq));
      d_samplesToShift = (int) ceil(samplesPerPeriod*0.5);
      d_differencesSL = new float[d_samplesToShift];
      d_differencesSR = new float[d_samplesToShift];

      dout("MaxSampleShift",d_samplesToShift);

      // Need at least 3 vectors since shifts can force off buffer conditions
      set_output_multiple(3);
    }

    /*
    * Our virtual destructor.
    */
    shift_and_measure_impl::~shift_and_measure_impl()
    {
    }

    float*
    shift_and_measure_impl::Shift_Left(const float *reference, const float *otherSignal, int &start, int &startDelay)
    {
      int maxShift = d_samplesToShift;
      for (int offset = 0; offset<maxShift; offset++)
      {
        d_differencesSL[offset] = 0;
        for (int overlap=0; overlap<(maxShift-offset); overlap++)
          d_differencesSL[offset] += fabs( reference[start + overlap] - otherSignal[startDelay + offset + overlap] );
      }

      return d_differencesSL;
    }

    float*
    shift_and_measure_impl::Shift_Right(const float *reference, const float *otherSignal, int &start, int &startDelay)
    {
      int maxShift = d_samplesToShift;
      for (int offset = 0; offset<maxShift; offset++)
      {
        d_differencesSR[offset] = 0;
        for (int overlap=0; overlap<(maxShift-offset); overlap++)
          d_differencesSR[offset] += fabs( reference[start + offset + overlap] - otherSignal[startDelay + overlap] );
      }

      return d_differencesSR;
    }

    int
    shift_and_measure_impl::Determine_Offset(float *SL, float *SR)
    {
      // Determine min value and index
      int minIndexSL = 0;
      int minIndexSR = 0;
      for (int i=0; i<d_samplesToShift; i++)
      {
        if (SL[i]<SL[minIndexSL])
          minIndexSL = i;

        if (SR[i]<SR[minIndexSR])
          minIndexSR = i;
      }

      // dout("minIndexSR",minIndexSR);
      // dout("minIndexSL",minIndexSL);
      // dout("SR[minIndexSR]",SR[minIndexSR])
      // dout("SL[minIndexSL]",SL[minIndexSL])

      // Return smallest error offset and adjust for direction
      if (SL[minIndexSL]<SR[minIndexSR])
        return -minIndexSL;
      else
        return minIndexSR;
    }

    int
    shift_and_measure_impl::work(int noutput_items,
      gr_vector_const_void_star &input_items,
      gr_vector_void_star &output_items)
      {
        // Inputs
        const float *ref = (const float *) input_items[0]; //reference signal
        const float *other = (const float *) input_items[1]; // to be corrected

        // Outputs
        int *out = (int *) output_items[0];

        int marker = 0;//keep track of vector processed
        int delayedMarker = 0;//shifter used in feedback

        // For function returns
        float *SL_Differences;
        float *SR_Differences;
        int currentDelay;

        // Operate over each input vector
        for (int items=0; items<(noutput_items+HIST_SIZE); items++)
        {
          // Delay signal according to lastest measurement
          delayedMarker = marker - (int) floor(d_lastDelay);

          //Make sure we have enough data for sliding (can be a problem with first and last vectors)
          if ((delayedMarker>=0)&&
             ((delayedMarker+d_samplesToShift)<(noutput_items*d_vlen)))
          {
            // Determine errors between signals when left shifting input 2
            SL_Differences = Shift_Left(ref, other, marker, delayedMarker);

            // Determine errors between signals when right shifting input 2
            SR_Differences = Shift_Right(ref, other, marker, delayedMarker);

            // Pick shift that provided minimum error
            currentDelay = Determine_Offset(SL_Differences, SR_Differences);

            // Update current best estimates
            d_lastDelay = d_lastDelay + d_mu*(float)currentDelay;
          }
          else
          {
            // dout("Skipped",noutput_items);
            // dout("marker",marker);dout("noutput_items",noutput_items);
          }

          // Check offset if over max delay
          if (d_lastDelay>d_samplesToShift)
            std::cout<<"WARNING: Shift past max value, offsets maybe > 90 Degrees\n";

          // Set out best integer of delay
          out[items] = (int) floor(d_lastDelay);

          // dout("d_lastDelay",d_lastDelay);

          // Increase index
          marker += d_vlen;
        }

        // Tell runtime system how many output items we produced.
        return noutput_items;
      }

  } /* namespace wifius */
} /* namespace gr */
