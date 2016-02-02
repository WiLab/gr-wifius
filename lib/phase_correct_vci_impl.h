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

#ifndef INCLUDED_WIFIUS_PHASE_CORRECT_VCI_IMPL_H
#define INCLUDED_WIFIUS_PHASE_CORRECT_VCI_IMPL_H

#include <wifius/phase_correct_vci.h>

namespace gr {
  namespace wifius {

    class phase_correct_vci_impl : public phase_correct_vci
    {
     private:
       size_t d_vlen;
       float d_mu;
       gr_complex d_currentShift;
       gr_complex *d_Shifted;
       float *d_Shifted_Real;
       float *d_error;
       float d_currentIndex;
       gr_complex *d_Shifts;
       bool d_debug;
       pmt::pmt_t d_enable_sync;

     public:
      phase_correct_vci_impl(float cal_tone_freq, float samp_rate, size_t vlen, float mu, bool debug);
      ~phase_correct_vci_impl();

      void set_enable_sync(pmt::pmt_t msg){d_enable_sync = msg;}

      float measure_error(float *ref, float *toSync);
      int min_error(float *error);

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_PHASE_CORRECT_VCI_IMPL_H */
