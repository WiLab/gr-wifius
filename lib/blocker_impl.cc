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
#include "blocker_impl.h"

namespace gr {
  namespace wifius {

    blocker::sptr
    blocker::make(bool default_state)
    {
      return gnuradio::get_initial_sptr
        (new blocker_impl(default_state));
    }

    /*
     * The private constructor
     */
    blocker_impl::blocker_impl(bool default_state)
      : gr::block("blocker",
              gr::io_signature::make(1, -1, sizeof(gr_complex)),
              gr::io_signature::make(1, -1, sizeof(gr_complex))),
      d_stop(default_state)
    {
      // Setup Input port
      message_port_register_in(pmt::mp("enable_stop"));
      set_msg_handler(pmt::mp("enable_stop"),
                      boost::bind(&blocker_impl::enable_stop, this, _1));
    }

    /*
     * Our virtual destructor.
     */
    blocker_impl::~blocker_impl()
    {
    }

    void
    blocker_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
        for(int i=0; i<ninput_items_required.size(); i++)
          ninput_items_required[i] = noutput_items;
    }

    int
    blocker_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {

        const char *iptr;
        char *optr;
        int inputs_used = noutput_items;// Always use all inputs

        if (!d_stop)//Output everything
        {
          for(size_t i = 0; i < input_items.size(); i++) {
            iptr = (const char *)input_items[i];
            optr = (char *)output_items[i];
            std::memcpy(optr, iptr, noutput_items*sizeof(gr_complex));
          }
        }
        else // Output Nothing
          noutput_items = 0;

        // Tell runtime system how many input items we consumed on
        // each input stream.
        consume_each (inputs_used);

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace wifius */
} /* namespace gr */
