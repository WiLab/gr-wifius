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
#include "find_scale_factor_impl.h"
#include <volk/volk.h>

namespace gr {
  namespace wifius {

    find_scale_factor::sptr
    find_scale_factor::make(float samp_rate, float cal_tone_freq)
    {
      return gnuradio::get_initial_sptr
        (new find_scale_factor_impl(samp_rate, cal_tone_freq));
    }

    /*
     * The private constructor
     */
    find_scale_factor_impl::find_scale_factor_impl(float samp_rate, float cal_tone_freq)
      : gr::sync_block("find_scale_factor",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(0, 0, 0))
    {

      d_samplesPerPeriod = (int) ceil(samp_rate/cal_tone_freq);

      set_history(d_samplesPerPeriod);// Need at least this many samples

      // Setup output message port
      message_port_register_out(pmt::mp("message"));
    }

    /*
     * Our virtual destructor.
     */
    find_scale_factor_impl::~find_scale_factor_impl()
    {
    }

    int
    find_scale_factor_impl::GetArgMax(float *signal, int start, int signalLength)
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

    int
    find_scale_factor_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *in = (const gr_complex *) input_items[0];

        // Convert to real
        float *in_real = new float[noutput_items];
        volk_32fc_deinterleave_real_32f(in_real, in, noutput_items);

        int samplesUsed = 0;
        int maxIndex = 0;

        // Determine max values and send out as messages
        while(samplesUsed<(noutput_items-d_samplesPerPeriod))
        {
          // Get index of max value
          maxIndex = GetArgMax(in_real, samplesUsed, d_samplesPerPeriod);

          // Convert complex to polymorphic type for message format
          pmt::pmt_t msg = pmt::from_complex(in[maxIndex]);

          // Send message out to port
          message_port_pub(pmt::mp("message"), msg);

          // Increment counter
          samplesUsed += d_samplesPerPeriod;
        }

        // Clean up
        delete in_real;

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace wifius */
} /* namespace gr */
