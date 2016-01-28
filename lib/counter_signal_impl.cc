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
#include "counter_signal_impl.h"

namespace gr {
  namespace wifius {

    counter_signal::sptr
    counter_signal::make(int num_samples, pmt::pmt_t msg, bool printEvent, std::string Message_To_Print)
    {
      return gnuradio::get_initial_sptr
        (new counter_signal_impl(num_samples, msg, printEvent, Message_To_Print));
    }

    /*
     * The private constructor
     */
    counter_signal_impl::counter_signal_impl(int num_samples, pmt::pmt_t msg, bool printEvent, std::string Message_To_Print)
      : gr::sync_block("counter_signal",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(0, 0, 0)),
          d_messageSent(false),
          d_samplesCounted(0),
          d_maxSamples(num_samples),
          d_msg(msg),
          d_printEvent(printEvent),
          d_Message_To_Print(Message_To_Print)
    {
      // Setup output message port
      message_port_register_out(pmt::mp("message"));
    }

    /*
     * Our virtual destructor.
     */
    counter_signal_impl::~counter_signal_impl()
    {
    }

    int
    counter_signal_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *in = (const gr_complex *) input_items[0];

        if (!d_messageSent)
        {
          // Count input samples
          d_samplesCounted += noutput_items;
          if (d_samplesCounted>=d_maxSamples)
          {
            message_port_pub(pmt::mp("message"), d_msg); // Send message out to port
            d_messageSent = true;
            if (d_printEvent)
            {
              std::cout<<"---------------------------\n";
              std::cout<<d_Message_To_Print<<std::endl;
              std::cout<<"---------------------------\n";
            }
          }
        }

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace wifius */
} /* namespace gr */
