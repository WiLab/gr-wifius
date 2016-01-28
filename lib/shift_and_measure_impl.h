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

#ifndef INCLUDED_WIFIUS_SHIFT_AND_MEASURE_IMPL_H
#define INCLUDED_WIFIUS_SHIFT_AND_MEASURE_IMPL_H

#include <wifius/shift_and_measure.h>

namespace gr {
  namespace wifius {

    class shift_and_measure_impl : public shift_and_measure
    {
     private:
      int d_samplesPerPeriod;
      size_t d_vlen;
      float *d_differencesSL;
      float *d_differencesSR;
      float d_lastDelay;
      float d_mu;
      int d_samplesToShift;
      int d_counter;
      float d_sigPeak;
      float d_error;
      bool d_debug;

     public:
      shift_and_measure_impl(float cal_tone_freq, float samp_rate, size_t vlen, float mu, bool debug);
      ~shift_and_measure_impl();

      int Get_Max_Index(const float *signal, int &start);
      float* Shift_Right(const float *reference, const float *otherSignal, int &start, int &startDelay);
      float* Shift_Left(const float *reference, const float *otherSignal, int &start, int &startDelay);
      int Determine_Offset(float *SL, float *SR);

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_SHIFT_AND_MEASURE_IMPL_H */
