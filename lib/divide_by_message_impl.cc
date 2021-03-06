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
#include "divide_by_message_impl.h"
#include <volk/volk.h>

namespace gr {
  namespace wifius {

    divide_by_message::sptr
    divide_by_message::make()
    {
      return gnuradio::get_initial_sptr
        (new divide_by_message_impl());
    }

    /*
     * The private constructor
     */
    divide_by_message_impl::divide_by_message_impl()
      : gr::sync_block("divide_by_message",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(1, 1, sizeof(gr_complex))),
        d_currentDivisor(gr_complex(1,0)),
        d_msgDivisor(gr_complex(1,0))
    {
      // Set up volk alignment
      const int alignment_multiple =
	     volk_get_alignment() / sizeof(gr_complex);
      set_alignment(std::max(1,alignment_multiple));

      // Setup Input port
      message_port_register_in(pmt::mp("set_divisor"));
      set_msg_handler(pmt::mp("set_divisor"),
                      boost::bind(&divide_by_message_impl::set_divisor, this, _1));
    }

    /*
     * Our virtual destructor.
     */
    divide_by_message_impl::~divide_by_message_impl()
    {
    }

    int
    divide_by_message_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *in = (const gr_complex *) input_items[0];
        gr_complex *out = (gr_complex *) output_items[0];
        int noi = noutput_items;

        // Update divisor from newest message
        if (abs(d_msgDivisor)>0.00001)//make sure it is not zero
          d_currentDivisor = gr_complex(1,0)/gr_complex(d_msgDivisor.real(),0);
        else
          d_currentDivisor = gr_complex(1,0);

        // Divide
        //for (int i=0; i<noutput_items; i++)
        //{
        //  out[i] = in[i] * d_currentDivisor;
        //}
        volk_32fc_s32fc_multiply_32fc(out, in, d_currentDivisor, noi);

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace wifius */
} /* namespace gr */
