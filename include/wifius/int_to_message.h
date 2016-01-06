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


#ifndef INCLUDED_WIFIUS_INT_TO_MESSAGE_H
#define INCLUDED_WIFIUS_INT_TO_MESSAGE_H

#include <wifius/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace wifius {

    /*!
     * \brief <+description of block+>
     * \ingroup wifius
     *
     */
    class WIFIUS_API int_to_message : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<int_to_message> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of wifius::int_to_message.
       *
       * To avoid accidental use of raw pointers, wifius::int_to_message's
       * constructor is in a private implementation
       * class. wifius::int_to_message::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_INT_TO_MESSAGE_H */

