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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "correct_input_impl.h"

namespace gr {
  namespace wifius {

    correct_input::sptr
    correct_input::make(size_t vlen)
    {
      return gnuradio::get_initial_sptr
        (new correct_input_impl(vlen));
    }

    /*
     * The private constructor
     */
    correct_input_impl::correct_input_impl(size_t vlen)
      : gr::block("correct_input",
              gr::io_signature::make(1, 1, sizeof(gr_complex)*vlen),
              gr::io_signature::make(1, 1, sizeof(gr_complex)*vlen)),
    d_Delay(0),
    d_delta(0),
    d_lastUpdate(0),
    d_vlen(vlen)
    {
      set_dly(0);

      // Setup Input port
      message_port_register_in(pmt::mp("set_delay"));
      set_msg_handler(pmt::mp("set_delay"),
                      boost::bind(&correct_input_impl::set_delay, this, _1));

    }

    /*
     * Our virtual destructor.
     */
    correct_input_impl::~correct_input_impl()
    {
    }

    void
    correct_input_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      // make sure input have noutput_items available
      ninput_items_required[0] = noutput_items;
    }

    void
    correct_input_impl::set_dly(int d)
    {
      // only set a new delta if there is a change in the delay; this
      // protects from quickly-repeated calls to this function that
      // would end with d_delta=0.
      if(d != dly()) {
        int old = dly();
        set_history(d+1);
        declare_sample_delay(history()-1);
        d_delta += dly() - old;
        std::cout<<"New d_delta: "<<d_delta<<std::endl;
      }
    }

    int
    correct_input_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      // Update d_delta, d_lastUpdate is from the message source input
      set_dly(d_lastUpdate);

      // Please note that the delay is in size vlen*sizeof(input)
      // Therefore if the input is a vector, the output is delayed
      // in vector multiples

      const char *iptr;
      char *optr;
      int cons, ret;

      // No change in delay; just memcpy ins to outs
      if(d_delta == 0) {
        for(size_t i = 0; i < input_items.size(); i++) {
          iptr = (const char *)input_items[i];
          optr = (char *)output_items[i];
          std::memcpy(optr, iptr, noutput_items*d_vlen*sizeof(gr_complex));
        }
        cons = noutput_items;
        ret = noutput_items;
      }

      // Skip over d_delta items on the input
      else if(d_delta < 0) {
        int n_to_copy, n_adj;
        int delta = -d_delta;
        n_to_copy = std::max(0, noutput_items-delta);
        n_adj = std::min(delta, noutput_items);
        for(size_t i = 0; i < input_items.size(); i++) {
          iptr = (const char *) input_items[i];
          optr = (char *) output_items[i];
          std::memcpy(optr, iptr+delta*d_vlen, n_to_copy*d_vlen*sizeof(gr_complex));
        }
        cons = noutput_items;
        ret = n_to_copy;
        delta -= n_adj;
        d_delta = -delta;
      }

      //produce but not consume (inserts zeros)
      else {  // d_delta > 0
        int n_from_input, n_padding;
        n_from_input = std::max(0, noutput_items-d_delta);
        n_padding = std::min(d_delta, noutput_items);
        for(size_t i = 0; i < input_items.size(); i++) {
          iptr = (const char *) input_items[i];
          optr = (char *) output_items[i];
          std::memset(optr, 0, n_padding*d_vlen*sizeof(gr_complex));
          std::memcpy(optr, iptr, n_from_input*d_vlen*sizeof(gr_complex));
        }
        cons = n_from_input;
        ret = noutput_items;
        d_delta -= n_padding;
      }

      consume_each(cons);
      return ret;
    }

  } /* namespace wifius */
} /* namespace gr */
