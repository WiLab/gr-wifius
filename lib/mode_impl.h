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

#ifndef INCLUDED_WIFIUS_MODE_IMPL_H
#define INCLUDED_WIFIUS_MODE_IMPL_H

#include <wifius/mode.h>

namespace gr {
  namespace wifius {

    class mode_impl : public mode
    {
     private:
       int *d_array;
       int d_min;
       int d_max;
       int d_memSize;
       bool d_MeasureLock;
       int d_SavedIndex;
       bool d_enableLocking;
       int d_samplesSinceLastSearch;
       int d_updatePeriod;

     public:
      mode_impl(int minValue, int maxValue, int memSize,
        bool enableLocking, int updatePeriod);
      ~mode_impl();

      int FindMode(int *array, int &arraySize);

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_MODE_IMPL_H */
