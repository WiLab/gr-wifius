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
#include "StreamsToRxx_impl.h"

#define d_num_sources 1

namespace gr {
  namespace wifius {

    StreamsToRxx::sptr
    StreamsToRxx::make(int num_antennas, int num_snapshots)
    {
      return gnuradio::get_initial_sptr
        (new StreamsToRxx_impl(num_antennas, num_snapshots));
    }

    /*
     * The private constructor
     */
    StreamsToRxx_impl::StreamsToRxx_impl(int num_antennas, int num_snapshots)
      : gr::sync_decimator("StreamsToRxx",
              gr::io_signature::make(num_antennas, num_antennas, sizeof(gr_complex)),
              gr::io_signature::make(1, 1, (num_antennas-d_num_sources)*num_antennas*sizeof(gr_complex)), num_snapshots),
      d_num_snapshots(num_snapshots),
      d_num_antennas(num_antennas)
    {
      // Predefine arrays
      d_X_mat = arma::zeros<arma::cx_mat>(num_antennas,num_snapshots);

      // Define output size
      d_output_size = sizeof(arma::cx_mat(num_antennas,num_antennas));
    }

    /*
     * Our virtual destructor.
     */
    StreamsToRxx_impl::~StreamsToRxx_impl()
    {
    }

    int
    StreamsToRxx_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      // Output is a matrix
      // arma::cx_mat *out = (arma::cx_mat *) output_items[0];
      gr_complex *out = (gr_complex *) output_items[0];

      int index = 0;
      for (int matrix=0; matrix<noutput_items; matrix++)
      {
        // Form matrix from inputs
        for (int i=0; i<input_items.size(); i++)
        {
          const gr_complex *in = (const gr_complex*) input_items[i];
          for(int s=0; s<d_num_snapshots; s++)
            d_X_mat(i,s) = in[s+(matrix*d_num_snapshots)];
        }
        // Create correlation matrix with inputs
        arma::cx_mat Rxx = d_X_mat * d_X_mat.t();// / (double)average_over;

        // Normalize
        // unsigned int average_over = d_nsamples / d_m;
        // x.reshape(d_m, average_over);	// (n_rows, n_cols)

        // Eigendecomposition
        arma::colvec eigvals;
        arma::cx_mat eigvec;
        arma::eig_sym(eigvals, eigvec, Rxx);

        // Remove columns that are only span noise
        arma::cx_mat NN = eigvec.cols(0,d_num_antennas-d_num_sources-1);
        
        // Output column by column
        for (int column=0; column<d_num_antennas; column++)
        {
            for (int row=0; row<(d_num_antennas-d_num_sources); row++)
            {
              out[index] = NN(column,row);
              index++;
            }
        }
      }

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace wifius */
} /* namespace gr */
