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


#ifndef INCLUDED_WIFIUS_COUNTER_SIGNAL_H
#define INCLUDED_WIFIUS_COUNTER_SIGNAL_H

#include <wifius/api.h>
#include <gnuradio/sync_block.h>
// #include <string>

namespace gr {
  namespace wifius {

    /*!
     * \brief <+description of block+>
     * \ingroup wifius
     *
     */
    class WIFIUS_API counter_signal : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<counter_signal> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of wifius::counter_signal.
       *
       * To avoid accidental use of raw pointers, wifius::counter_signal's
       * constructor is in a private implementation
       * class. wifius::counter_signal::make is the public interface for
       * creating new instances.
       */
      static sptr make(int num_samples, pmt::pmt_t msg, bool printEvent, std::string Message_To_Print);
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_COUNTER_SIGNAL_H */
