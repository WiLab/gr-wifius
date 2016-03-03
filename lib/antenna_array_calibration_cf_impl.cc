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
#include "antenna_array_calibration_cf_impl.h"
#include <armadillo>
#include <gnuradio/math.h>

#define PI 3.14159265359

namespace gr {
  namespace wifius {

    antenna_array_calibration_cf::sptr
    antenna_array_calibration_cf::make(float angle, float norm_antenna_spacing, int num_antennas, int num_snapshots)
    {
      return gnuradio::get_initial_sptr
        (new antenna_array_calibration_cf_impl(angle, norm_antenna_spacing, num_antennas, num_snapshots));
    }

    /*
     * The private constructor
     */
    antenna_array_calibration_cf_impl::antenna_array_calibration_cf_impl(float angle, float norm_antenna_spacing, int num_antennas, int num_snapshots)
      : gr::sync_decimator("antenna_array_calibration_cf",
              gr::io_signature::make(num_antennas, num_antennas, sizeof(gr_complex)),
              gr::io_signature::make(2, 2, num_antennas*sizeof(float)), num_snapshots),
      d_num_antennas(num_antennas),
      d_norm_antenna_spacing(norm_antenna_spacing),
      d_angle(angle),
      d_num_snapshots(num_snapshots),
      d_hold_estimate(true)
    {
      //// Create processing matrices

      // Wavelength Vector
      arma::colvec K;
      K << PI*cos(angle*PI/180) << PI*sin(angle*PI/180) << 0 << arma::endr;

      // Antenna coordinates, only assuming ULA for now
      arma::mat r(num_antennas,3);
      for (int ant=0; ant<num_antennas; ant++)
        r(ant,0) = ant*norm_antenna_spacing;

      // Create mapping from antenna to delays
      arma::colvec rK = r*K;
      arma::colvec zero = rK;
      arma::cx_colvec crK(zero.zeros(),-2*rK);

      arma::cx_colvec ro = arma::exp(crK);

      // Create processing matrices
      d_O = arma::diagmat(ro);
      d_O_h = arma::diagmat(ro).t();

      // Storage variables
      arma::cx_mat tmp(num_antennas,num_snapshots);
      d_X = tmp;
      d_Rxx = tmp;
      d_saved_gains = new float[num_antennas];
      d_saved_phases = new float[num_antennas];
      for (int i=0; i<num_antennas; i++)
      {
        d_saved_gains[i] = 1.0;
        d_saved_phases[i] = 0.0;
      }

      // Setup Input port
      message_port_register_in(pmt::mp("enable_hold"));
      set_msg_handler(pmt::mp("enable_hold"),
                      boost::bind(&antenna_array_calibration_cf_impl::enable_hold, this, _1));
    }

    /*
     * Our virtual destructor.
     */
    antenna_array_calibration_cf_impl::~antenna_array_calibration_cf_impl()
    {
    }

    int
    antenna_array_calibration_cf_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      float *GainEst = (float *) output_items[0];
      float *PhaseEst = (float *) output_items[1];

      gr_complex *inputData;

      int outIndex = 0;

      if (!d_hold_estimate)
      {
        for (int vec=0; vec<noutput_items; vec++)
        {
          // Form matrix from inputs
          for (int i=0; i<input_items.size(); i++)
          {
            const gr_complex *in = (const gr_complex*) input_items[i];
            for(int s=0; s<d_num_snapshots; s++)
            d_X(i,s) = in[s+(vec*d_num_snapshots)];
          }

          // Autocorrelate
          arma::cx_mat Rxx = d_X*d_X.t();

          // Process correlation matrix
          arma::cx_mat OhRO = d_O_h*Rxx*d_O;

          // Build outputs
          gr_complex gamma2 = (gr_complex) sqrt(arma::as_scalar(OhRO(0,0)));

          for(int output=0; output<d_num_antennas; output++)
          {
            if (output>0)
            {
              gr_complex val = ((gr_complex) arma::as_scalar(OhRO(output,0))/gamma2);
              GainEst[outIndex] = (float) abs(val);
              PhaseEst[outIndex] = (float)  gr::fast_atan2f(val.imag(),val.real());
            }
            else
            {
              GainEst[outIndex] = (float) abs(gamma2);
              PhaseEst[outIndex] = (float) gr::fast_atan2f(gamma2.imag(),gamma2.real());
            }
            outIndex++;
          }
          // Save outputs
          memcpy(d_saved_gains, GainEst-d_num_antennas, d_num_antennas*sizeof(float));
          memcpy(d_saved_phases,  PhaseEst-d_num_antennas, d_num_antennas*sizeof(float));
        }
      }
      else
      {
        // std::cout<<"Skipping\n";
        for (int vec=0; vec<noutput_items; vec++)
        {
          memcpy(GainEst+vec*d_num_antennas,  d_saved_gains,   d_num_antennas*sizeof(float));
          memcpy(PhaseEst+vec*d_num_antennas, d_saved_phases,  d_num_antennas*sizeof(float));
        }
      }

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace wifius */
} /* namespace gr */
