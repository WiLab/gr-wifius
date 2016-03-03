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

#ifndef INCLUDED_WIFIUS_DOA_MUSIC_VCVF_IMPL_H
#define INCLUDED_WIFIUS_DOA_MUSIC_VCVF_IMPL_H

#include <wifius/doa_music_vcvf.h>

// Need linear algebra libraries
#include <armadillo>

#include <vector>

namespace gr {
  namespace wifius {

    class doa_music_vcvf_impl : public doa_music_vcvf
    {
     private:
       arma::cx_mat d_X_mat;
       std::vector< arma::cx_rowvec* > d_SS;
       int d_num_antennas;
       int d_source_signals;
       int d_num_samples;

     public:
      doa_music_vcvf_impl(int num_antennas, float norm_antenna_spacing, int source_signals, float frequency_resolution, int num_samples);
      ~doa_music_vcvf_impl();

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_DOA_MUSIC_VCVF_IMPL_H */
