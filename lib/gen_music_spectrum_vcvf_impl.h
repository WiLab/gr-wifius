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

#ifndef INCLUDED_WIFIUS_GEN_MUSIC_SPECTRUM_VCVF_IMPL_H
#define INCLUDED_WIFIUS_GEN_MUSIC_SPECTRUM_VCVF_IMPL_H

#include <wifius/gen_music_spectrum_vcvf.h>

// Need linear algebra libraries
#include <armadillo>

namespace gr {
  namespace wifius {

    class gen_music_spectrum_vcvf_impl : public gen_music_spectrum_vcvf
    {
     private:
       arma::cx_mat d_X_mat;
       std::vector< arma::cx_rowvec* > d_SS;
       int d_num_antennas;
       int d_num_sources;
       float d_min_degree;
       float d_max_degree;
       float d_step;
       float d_norm_spacing;
       int d_snapshots;

     public:
      gen_music_spectrum_vcvf_impl(int num_antennas, int num_sources, float min_degree, float max_degree, float step, float norm_spacing, int num_snapshots);
      ~gen_music_spectrum_vcvf_impl();

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_GEN_MUSIC_SPECTRUM_VCVF_IMPL_H */
