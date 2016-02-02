/* -*- c++ -*- */
/*
 * Copyright 2016 Travis F. Collins (travisfcollins@gmail.com).
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
#include "phase_correct_vci_impl.h"
#include <volk/volk.h>

#define PI 3.14159265359
#define dout(X,Y) {if(d_debug){std::cout<<X<<": "<<Y<<std::endl;}}

// The purpose of this block is to measure the phase difference between two
// input signals that are both sinusoids.  The output will be a complex value of
// rotation to multiple the offset signal by to correctly phase align them.
//
// The first input will act as the reference and the second is to be corrected


namespace gr {
  namespace wifius {

    phase_correct_vci::sptr
    phase_correct_vci::make(float cal_tone_freq, float samp_rate, size_t vlen, float mu, bool debug)
    {
      return gnuradio::get_initial_sptr
        (new phase_correct_vci_impl(cal_tone_freq, samp_rate, vlen, mu, debug));
    }

    /*
     * The private constructor
     */
    phase_correct_vci_impl::phase_correct_vci_impl(float cal_tone_freq, float samp_rate, size_t vlen, float mu, bool debug)
      : gr::sync_block("phase_correct_vci",
              gr::io_signature::make(2, 2, sizeof(gr_complex)*vlen),
              gr::io_signature::make(1, 1, sizeof(gr_complex)*vlen)),
        d_vlen(vlen),
        d_mu(mu),
        d_currentShift(gr_complex(0,0)),
        d_debug(debug),
        d_enable_sync(pmt::PMT_T), // Set true
        d_currentIndex(180)//set in the middle
    {

      set_output_multiple(3);

      // Preallocate tmp values
      d_Shifted = new gr_complex[d_vlen];
      d_Shifted_Real = new float[d_vlen];
      d_error = new float[360];

      // Precalculate all phase shifts
      d_Shifts = new gr_complex[360];
      for (int degree=-180; degree<180; degree++)
        d_Shifts[degree+180] = gr_complex( cos(degree*PI/180), sin(degree*PI/180) );

      // Setup Input port
      message_port_register_in(pmt::mp("set_enable_sync"));
      set_msg_handler(pmt::mp("set_enable_sync"),
      boost::bind(&phase_correct_vci_impl::set_enable_sync, this, _1));

    }

    float
    phase_correct_vci_impl::measure_error(float *ref, float *toSync)
    {
      float error = 0;
      for(int k=0; k<d_vlen; k++)
        error += fabs(ref[k]-toSync[k]);

      return error;
    }

    int
    phase_correct_vci_impl::min_error(float *error)
    {
        int indexOfMinError = 0;
        for(int k=0; k<360; k++)
        {
          if (error[k]<error[indexOfMinError])
              indexOfMinError = k;
        }

        return indexOfMinError;
    }

    /*
     * Our virtual destructor.
     */
    phase_correct_vci_impl::~phase_correct_vci_impl()
    {
    }

    int
    phase_correct_vci_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *ref = (const gr_complex *) input_items[0];
        const gr_complex *toSync = (const gr_complex *) input_items[1];
        gr_complex *out = (gr_complex *) output_items[0];

        int nSamples = noutput_items*d_vlen;
        int minErrorIndex;
        int indexError;

        // Sync Disabled
        if (d_enable_sync==pmt::PMT_F)
        {
          // Shift signal by angle
          volk_32fc_s32fc_multiply_32fc(out, toSync, d_Shifts[(int) floor(d_currentIndex)], nSamples);
          // Tell runtime system how many output items we produced.
          return noutput_items;
        }

        // Convert ref to real
        float *refReal = new float[nSamples];
        volk_32fc_deinterleave_real_32f(refReal, ref, nSamples);

        for(int vec=0; vec<noutput_items; vec++)
        {
          for(int d=0; d<360; d++)
          {
            // Shift signal by angle
            volk_32fc_s32fc_multiply_32fc(d_Shifted, toSync+(vec*d_vlen), d_Shifts[d], d_vlen);
            // Convert to Real
            volk_32fc_deinterleave_real_32f(d_Shifted_Real, d_Shifted, d_vlen);

            // Get error between signals
            d_error[d] = measure_error(refReal+(vec*d_vlen), d_Shifted_Real);
          }

          // Determine which shift gave the minimum error
          minErrorIndex = min_error(d_error);

          // How far are we from current answer?
          indexError = minErrorIndex - d_currentIndex;
          dout("indexError",indexError);

          // Update best index
          d_currentIndex = d_currentIndex + d_mu*indexError;
          dout("d_currentIndex",d_currentIndex);

          // Check validity
          if ((d_currentIndex<0) || (d_currentIndex>359))
          {
            dout("Reset",0);
            d_currentIndex = 0;
          }

          // // Send to output
          // out[vec] = d_Shifts[(int) floor(d_currentIndex)];
          //
          // Shift signal by angle
          volk_32fc_s32fc_multiply_32fc(out+(vec*d_vlen), toSync+(vec*d_vlen), d_Shifts[(int) floor(d_currentIndex)], d_vlen);
        }

        // Clean up
        delete refReal;

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace wifius */
} /* namespace gr */
