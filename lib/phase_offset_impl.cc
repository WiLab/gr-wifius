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
#include "phase_offset_impl.h"

#include <cmath> //needed to exp

namespace gr {
  namespace wifius {

    phase_offset::sptr
    phase_offset::make(float offset)
    {
      return gnuradio::get_initial_sptr
        (new phase_offset_impl(offset));
    }

    /*
     * The private constructor
     */
    phase_offset_impl::phase_offset_impl(float offset)
      : gr::sync_block("phase_offset",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(1, 1, sizeof(gr_complex)))
    {
      // Phase delay by 'offset' radians: y = x*exp(-i*N);
      d_offset;

    }

    /*
     * Our virtual destructor.
     */
    phase_offset_impl::~phase_offset_impl()
    {
    }

    int
    phase_offset_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const float *in = (const float *) input_items[0];
        float *out = (float *) output_items[0];

        // Do <+signal processing+>

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace wifius */
} /* namespace gr */
