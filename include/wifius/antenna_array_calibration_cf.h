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


#ifndef INCLUDED_WIFIUS_ANTENNA_ARRAY_CALIBRATION_CF_H
#define INCLUDED_WIFIUS_ANTENNA_ARRAY_CALIBRATION_CF_H

#include <wifius/api.h>
#include <gnuradio/sync_decimator.h>

namespace gr {
  namespace wifius {

    /*!
     * \brief <+description of block+>
     * \ingroup wifius
     *
     */
    class WIFIUS_API antenna_array_calibration_cf : virtual public gr::sync_decimator
    {
     public:
      typedef boost::shared_ptr<antenna_array_calibration_cf> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of wifius::antenna_array_calibration_cf.
       *
       * To avoid accidental use of raw pointers, wifius::antenna_array_calibration_cf's
       * constructor is in a private implementation
       * class. wifius::antenna_array_calibration_cf::make is the public interface for
       * creating new instances.
       */
      static sptr make(float angle, float norm_antenna_spacing, int num_antennas, int num_snapshots);
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_ANTENNA_ARRAY_CALIBRATION_CF_H */
