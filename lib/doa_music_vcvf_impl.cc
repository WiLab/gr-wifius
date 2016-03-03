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
#include "doa_music_vcvf_impl.h"

#define PI 3.14159265359

namespace gr {
  namespace wifius {

    doa_music_vcvf::sptr
    doa_music_vcvf::make(int num_antennas, float norm_antenna_spacing, int source_signals, float frequency_resolution, int num_samples)
    {
      return gnuradio::get_initial_sptr
        (new doa_music_vcvf_impl(num_antennas, norm_antenna_spacing, source_signals, frequency_resolution, num_samples));
    }

    /*
     * The private constructor
     */
    doa_music_vcvf_impl::doa_music_vcvf_impl(int num_antennas, float norm_antenna_spacing, int source_signals, float frequency_resolution, int num_samples)
      : gr::sync_block("doa_music_vcvf",
              gr::io_signature::make(num_antennas, num_antennas, num_samples*sizeof(gr_complex)),
              gr::io_signature::make(1, 1, ((int) 181/frequency_resolution)*sizeof(float))),
      d_num_antennas(num_antennas),
      d_source_signals(source_signals),
      d_num_samples(num_samples)
    {
      // Predefine arrays
      d_X_mat = arma::zeros<arma::cx_mat>(num_antennas,num_samples);

      // Pregenerate antenna responses
      arma::cx_rowvec *rv;
      for(int degrees=-90; degrees<90; degrees=degrees+frequency_resolution)
      {
        rv = new arma::cx_rowvec(num_antennas);
        for (int antenna=0; antenna<num_antennas; antenna++)
          (*rv)(antenna) = exp(gr_complex(0,-2*antenna*PI*norm_antenna_spacing*sin(degrees/180*PI)));

        d_SS.push_back(rv);
      }
    }

    /*
     * Our virtual destructor.
     */
    doa_music_vcvf_impl::~doa_music_vcvf_impl()
    {
    }

    int
    doa_music_vcvf_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        float *out = (float *) output_items[0];

        for (int vec=0; vec<noutput_items; vec++)
        {
          // Form matrix from inputs
          for (int i=0; i<input_items.size(); i++)
          {
            const gr_complex *in = (const gr_complex*) input_items[i];
            for(int s=0; s<d_num_samples; s++)
              d_X_mat(i,s) = in[s+(vec*d_num_samples)];
          }
          // Create correlation matrix with inputs
          // unsigned int average_over = d_nsamples / d_m;
          // x.reshape(d_m, average_over);	// (n_rows, n_cols)
          //std::cout << "size of d_X_mat: " << size(d_X_mat) << std::endl;
          arma::cx_mat R = d_X_mat * d_X_mat.t();// / (double)average_over;

          // Eigendecomposition
          arma::colvec eigvals;
          arma::cx_mat eigvec;
          arma::eig_sym(eigvals, eigvec, R);

          // Remove unused columns
          arma::cx_mat NN(d_num_antennas,d_num_antennas-d_source_signals);
          for (int col=0; col<(d_num_antennas-d_source_signals); col++)
          {
            for (int row=0; row<d_num_antennas; row++)
                NN(row,col) = eigvec(row,col);
          }
          // Create MUSIC Spectrum
          for (int theta=0; theta<d_SS.size(); theta++)
          {
            arma::cx_mat NNN = NN*NN.t();
            arma::cx_mat SS_NNN = (*(d_SS[theta]))  * NNN;
            arma::cx_mat P = SS_NNN * ((*(d_SS[theta])).t());
            out[theta+(vec*d_num_samples)] = (float) abs(gr_complexd(1,0)/P(0,0));
          }

        }

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace wifius */
} /* namespace gr */
