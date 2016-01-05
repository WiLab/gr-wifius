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


#ifndef INCLUDED_WIFIUS_CORRECT_INPUT_H
#define INCLUDED_WIFIUS_CORRECT_INPUT_H

#include <wifius/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace wifius {

    /*!
     * \brief <+description of block+>
     * \ingroup wifius
     *
     */
    class WIFIUS_API correct_input : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<correct_input> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of wifius::correct_input.
       *
       * To avoid accidental use of raw pointers, wifius::correct_input's
       * constructor is in a private implementation
       * class. wifius::correct_input::make is the public interface for
       * creating new instances.
       */
       static sptr make(size_t vlen);


       virtual int dly() const = 0;

       /*!
        * \brief Reset the delay.
        * \param d change the delay value. This can be a positive or
        * negative value.
        */
       virtual void set_dly(int d) = 0;
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_CORRECT_INPUT_H */
