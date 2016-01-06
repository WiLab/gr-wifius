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

#ifndef INCLUDED_WIFIUS_FIND_SCALE_FACTOR_IMPL_H
#define INCLUDED_WIFIUS_FIND_SCALE_FACTOR_IMPL_H

#include <wifius/find_scale_factor.h>

namespace gr {
  namespace wifius {

    class find_scale_factor_impl : public find_scale_factor
    {
     private:
      int d_samplesPerPeriod;

     public:
      find_scale_factor_impl(float samp_rate, float cal_tone_freq);
      ~find_scale_factor_impl();

      int GetArgMax(float *input, int start, int signalLength);

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_FIND_SCALE_FACTOR_IMPL_H */
