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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "int_to_message_impl.h"

namespace gr {
  namespace wifius {

    int_to_message::sptr
    int_to_message::make()
    {
      return gnuradio::get_initial_sptr
        (new int_to_message_impl());
    }

    /*
     * The private constructor
     */
    int_to_message_impl::int_to_message_impl()
      : gr::sync_block("int_to_message",
              gr::io_signature::make(1, 1, sizeof(int)),
              gr::io_signature::make(0, 0, 0))
    {
      // Setup output message port
      message_port_register_out(pmt::mp("message"));
    }

    /*
     * Our virtual destructor.
     */
    int_to_message_impl::~int_to_message_impl()
    {
    }

    int
    int_to_message_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const int *in = (const int *) input_items[0];

        // Number of items from input to use
        int nitems = 1;//(int) noutput_items;

        for (int i=0; i<nitems; i++)
        {
          // Convert integer to polymorphic type for message format
          pmt::pmt_t msg = pmt::from_double(in[0]);

          // Send message out to port
          message_port_pub(pmt::mp("message"), msg);
        }

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace wifius */
} /* namespace gr */
