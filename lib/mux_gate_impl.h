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

#ifndef INCLUDED_WIFIUS_MUX_GATE_IMPL_H
#define INCLUDED_WIFIUS_MUX_GATE_IMPL_H

#include <wifius/mux_gate.h>

namespace gr {
  namespace wifius {

    class mux_gate_impl : public mux_gate
    {
     private:
      boost::atomic<int> d_selection;
      int d_num_outputs;

     public:
      mux_gate_impl(int num_outputs, int default_output);
      ~mux_gate_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      // Callback for message
      void select_output(pmt::pmt_t msg)
        {
          int tmp = d_selection;
          int newVal = pmt::to_long(msg);
          if(newVal!=tmp)
            d_selection = newVal;
        }

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_MUX_GATE_IMPL_H */
