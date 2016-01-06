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

#ifndef INCLUDED_WIFIUS_DIVIDE_BY_MESSAGE_IMPL_H
#define INCLUDED_WIFIUS_DIVIDE_BY_MESSAGE_IMPL_H

#include <wifius/divide_by_message.h>

namespace gr {
  namespace wifius {

    class divide_by_message_impl : public divide_by_message
    {
     private:
       gr_complex d_msgDivisor; // Updated each time a message is received
       gr_complex d_currentDivisor; // Updated at start of each work call

     public:
      divide_by_message_impl();
      ~divide_by_message_impl();

      // Custom functions
      void set_divisor(pmt::pmt_t msg){d_msgDivisor = pmt::to_complex(msg);}

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_DIVIDE_BY_MESSAGE_IMPL_H */
