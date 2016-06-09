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
#include "gen_music_spectrum_vcvf_impl.h"

#define PI 3.14159265359

namespace gr {
  namespace wifius {


    std::vector<int>
    get_in_sizeofs(size_t item_size, int snapshots, int num_antennas)
      {
        std::vector<int> out_sizeofs;
        // Add for first 2 inputs
        out_sizeofs.push_back(sizeof(float)*num_antennas);
        out_sizeofs.push_back(sizeof(float)*num_antennas);
        // Add rest for antennas
        for(unsigned int i = 0; i < num_antennas; i++)
        {
          out_sizeofs.push_back(item_size*snapshots);
        }
        return out_sizeofs;
      }

    gen_music_spectrum_vcvf::sptr
    gen_music_spectrum_vcvf::make(int num_antennas, int num_sources, float min_degree, float max_degree, float step, float norm_spacing, int snapshots)
    {
      return gnuradio::get_initial_sptr
        (new gen_music_spectrum_vcvf_impl(num_antennas, num_sources, min_degree, max_degree, step, norm_spacing, snapshots));
    }

    /*
     * The private constructor
     */
    gen_music_spectrum_vcvf_impl::gen_music_spectrum_vcvf_impl(int num_antennas, int num_sources, float min_degree, float max_degree, float step, float norm_spacing, int snapshots)
      : gr::sync_block("gen_music_spectrum_vcvf",
              gr::io_signature::makev(num_antennas+2, num_antennas+2, get_in_sizeofs(sizeof(gr_complex), snapshots, num_antennas)),
              gr::io_signature::make(1, 1, floor( (max_degree-min_degree)/step )*sizeof(float))),
      d_num_antennas(num_antennas),
      d_num_sources(num_sources),
      d_min_degree(min_degree),
      d_max_degree(max_degree),
      d_step(step),
      d_norm_spacing(norm_spacing),
      d_snapshots(snapshots)
    {
      // // Pregenerate antenna responses
      // arma::cx_rowvec *rv;
      // for(int degrees=min_degree; degrees<max_degree; degrees=degrees+step)
      // {
      //   rv = new arma::cx_rowvec(num_antennas);
      //   for (int antenna=0; antenna<num_antennas; antenna++)
      //     (*rv)(antenna) = exp(gr_complex(0,-2*antenna*PI*norm_spacing*sin( ((double)degrees)/180*PI)));
      //
      //   d_SS.push_back(rv);
      // }

      // Predefine arrays
      d_X_mat = arma::zeros<arma::cx_mat>(num_antennas, snapshots);
    }

    /*
     * Our virtual destructor.
     */
    gen_music_spectrum_vcvf_impl::~gen_music_spectrum_vcvf_impl()
    {
    }

    int
    gen_music_spectrum_vcvf_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      // Output is vector of MuSIC Spectrum
      float *out = (float *) output_items[0];

      // Calibration data (num_antennas X 1)
      float *GainEsts = (float *) input_items[0];
      float *PhaseEsts = (float *) input_items[1];

      // Tmp Values
      arma::cx_mat NN(d_num_antennas, (d_num_antennas-d_num_sources));
      arma::cx_rowvec rv(d_num_antennas);
      arma::cx_colvec ComplexGain(d_num_antennas);
      int index = 0;
      int outIndex = 0;

      // Debugging
      int maxSamples = noutput_items*( (int) floor( (d_max_degree-d_min_degree)/d_step ) );

      // Process each vector
      for (int matrix=0; matrix<noutput_items; matrix++)
      {
        // Form matrix from inputs, rows are each input
        for (int i=2; i<input_items.size(); i++)
        {
          const gr_complex *in = (const gr_complex*) input_items[i];
          for(int s=0; s<d_snapshots; s++)
            d_X_mat(i-2,s) = in[s+(matrix*d_snapshots)];
        }
        // Create correlation matrix with inputs
        arma::cx_mat Rxx = d_X_mat * d_X_mat.t();// / (double)average_over;

        // Normalize
        // unsigned int average_over = d_nsamples / d_m;
        // x.reshape(d_m, average_over);	// (n_rows, n_cols)

        // Correct will channel estimates
        int index = matrix*d_num_antennas;
        for (int i=0; i<d_num_antennas; i++)
        {
          ComplexGain(i) = GainEsts[index]*exp(gr_complex(0,PhaseEsts[index]));
          index++;
        }
        Rxx = Rxx/(ComplexGain * ComplexGain.t());

        // Eigendecomposition
        arma::colvec eigvals;
        arma::cx_mat eigvec;
        arma::eig_sym(eigvals, eigvec, Rxx);

        // Remove columns that are only span noise
        arma::cx_mat NN = eigvec.cols(0,d_num_antennas-d_num_sources-1);

        // Create MUSIC Spectrum
        for (int degree=d_min_degree; degree<d_max_degree; degree = degree+d_step)
        {
          // Form antenna response
          for (int antenna=0; antenna<d_num_antennas; antenna++)
            rv(antenna) = exp(gr_complex(0,-2*antenna*PI*d_norm_spacing*sin( ((double)degree)/180*PI)));

          // Excite array response
          arma::cx_mat P = rv  * NN*NN.t() * (rv.t());

          // Output music spectrum in log scale
          out[outIndex] = (float) 10*log10( abs(gr_complexd(1,0)/P(0,0)) );
          outIndex++;

          // // Degree increments can go off max outputs sometimes
          // if (outIndex>maxSamples)
          // {
          //   std::cout<<"Premature exit\n";
          //   return noutput_items;
          // }
        }

      }

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace wifius */
} /* namespace gr */
