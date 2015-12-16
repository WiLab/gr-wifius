/* -*- c++ -*- */
/*
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
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

#ifndef INCLUDED_WIFIUS_DELAY_SIG_IMPL_H
#define INCLUDED_WIFIUS_DELAY_SIG_IMPL_H

#include <wifius/delay_sig.h>

namespace gr {
  namespace wifius {

    class delay_sig_impl : public delay_sig
    {
     private:
       int d_delta;
       int d_Delay;
       int d_vlen;
       gr::thread::mutex d_mutex_delay;

       void forecast (int noutput_items, gr_vector_int &ninput_items_required);

     public:
      delay_sig_impl(size_t vlen);
      ~delay_sig_impl();

      // Custom functions
      int dly() const { return history()-1; }
      void set_dly(int d);

      // Where all the action really happens
      int general_work(int noutput_items,
		       gr_vector_int &ninput_items,
		       gr_vector_const_void_star &input_items,
		       gr_vector_void_star &output_items);
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_DELAY_SIG_IMPL_H */
