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

#ifndef INCLUDED_WIFIUS_ANTENNA_ARRAY_CALIBRATION_CF_IMPL_H
#define INCLUDED_WIFIUS_ANTENNA_ARRAY_CALIBRATION_CF_IMPL_H

#include <wifius/antenna_array_calibration_cf.h>
#include <armadillo>

namespace gr {
  namespace wifius {

    class antenna_array_calibration_cf_impl : public antenna_array_calibration_cf
    {
     private:
       int d_num_antennas;
       float d_norm_antenna_spacing;
       float d_angle;
       int d_num_snapshots;
       arma::cx_mat d_O;
       arma::cx_mat d_O_h;
       arma::cx_mat d_X;
       arma::cx_mat d_Rxx;
       bool d_hold_estimate;
       float *d_saved_gains;
       float *d_saved_phases;

     public:
      antenna_array_calibration_cf_impl(float angle, float norm_antenna_spacing, int num_antennas, int num_snapshots);
      ~antenna_array_calibration_cf_impl();

      void enable_hold(pmt::pmt_t msg)
        {
          d_hold_estimate = false;
          if(pmt::to_double(msg)>0)
            d_hold_estimate = true;
        }

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_ANTENNA_ARRAY_CALIBRATION_CF_IMPL_H */
