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

#ifndef INCLUDED_WIFIUS_COUNTER_SIGNAL_IMPL_H
#define INCLUDED_WIFIUS_COUNTER_SIGNAL_IMPL_H

#include <wifius/counter_signal.h>

namespace gr {
  namespace wifius {

    class counter_signal_impl : public counter_signal
    {
     private:
       bool d_messageSent;
       int d_samplesCounted;
       int d_maxSamples;
       pmt::pmt_t d_msg;
       bool d_printEvent;

     public:
      counter_signal_impl(int num_samples, pmt::pmt_t msg, bool printEvent);
      ~counter_signal_impl();

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_COUNTER_SIGNAL_IMPL_H */
