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
#include "mux_gate_impl.h"
#include <iostream>

namespace gr {
  namespace wifius {

    mux_gate::sptr
    mux_gate::make(int num_outputs, int default_output)
    {
      return gnuradio::get_initial_sptr
        (new mux_gate_impl(num_outputs, default_output));
    }

    /*
     * The private constructor
     */
    mux_gate_impl::mux_gate_impl(int num_outputs, int default_output)
      : gr::block("mux_gate",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(1, -1, sizeof(gr_complex))),
        d_num_outputs(num_outputs)
    {
        // Setup Input port
        message_port_register_in(pmt::mp("select_output"));
        set_msg_handler(pmt::mp("select_output"),
                        boost::bind(&mux_gate_impl::select_output, this, _1));

        // Set default
        d_selection = default_output;
    }

    /*
     * Our virtual destructor.
     */
    mux_gate_impl::~mux_gate_impl()
    {
    }

    void
    mux_gate_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
        for(int i=0; i<ninput_items_required.size(); i++)
          ninput_items_required[i] = noutput_items;
    }

    int
    mux_gate_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
        const char *iptr;
        char *optr;
        int inputs_used = noutput_items;// Always use all inputs

        int output = d_selection; // Move to non-atomic

        for(int i = 0; i < d_num_outputs; i++)
        {
            if (output==i)
            {
                iptr = (const char *)input_items[0];
                optr = (char *)output_items[i];
                std::memcpy(optr, iptr, noutput_items*sizeof(gr_complex));
                produce(i, noutput_items);
            }
            else
                produce(i, 0);
        }

        // Tell runtime system how many input items we consumed on
        // each input stream.
        consume_each (inputs_used);

        // Magical
        return WORK_CALLED_PRODUCE; // -2
    }

  } /* namespace wifius */
} /* namespace gr */
