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
#include "mode_impl.h"

#include <stdexcept>

namespace gr {
  namespace wifius {

    mode::sptr
    mode::make(int minValue, int maxValue, int memSize, bool enableLocking)
    {
      return gnuradio::get_initial_sptr
        (new mode_impl(minValue, maxValue, memSize, enableLocking));
    }

    /*
     * The private constructor
     */
    mode_impl::mode_impl(int minValue, int maxValue, int memSize, bool enableLocking)
      : gr::sync_block("mode",
              gr::io_signature::make(1, 1, sizeof(int)),
              gr::io_signature::make(1, 1, sizeof(int))),
              d_min(minValue),
              d_max(maxValue),
              d_memSize(memSize),
              d_MeasureLock(false),
              d_enableLocking(enableLocking)
    {
      // Initialize tally array
      d_array = new int[maxValue-minValue+1];
      std::fill(d_array,d_array+maxValue-minValue+1,0);

      // Set memory size
      set_history(d_memSize);
    }

    /*
     * Our virtual destructor.
     */
    mode_impl::~mode_impl()
    {
    }

    int
    mode_impl::FindMode(int *array, int &arraySize)
    {
      int mostCommonIndex = 0;
      int sum = 0;
      for (int i=0; i<arraySize; i++)
      {
        sum = sum + array[i];
        if (array[i]>array[mostCommonIndex])
          mostCommonIndex = i;
      }
      //std::cout<<"Most Common Tally Index: "<<mostCommonIndex<<" ("<<sum<<")"<<std::endl;
      if (sum==array[mostCommonIndex])
      {
        d_MeasureLock = true;
        //std::cout<<"Locked Estimate\n";
      }

      return mostCommonIndex;
    }

    int
    mode_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const int *in = (const int *) input_items[0];
        int *out = (int *) output_items[0];

        int arrayAbleIndex = 0;
        int arraySize = d_max-d_min+1;
        int mostCommonIndex = 0;
        int indexToBeRemoved = 0;
        int myMin = d_min;

        // First d_memSize-1 samples are from the past
        for (int i=0; i<noutput_items; i++)
        {
            // Make input 0->N, by biasing by minimum value
            arrayAbleIndex = in[i+d_memSize] - myMin;
            // if ((arrayAbleIndex<0)||(arrayAbleIndex>d_max-myMin))
            //   throw std::runtime_error ("Input out of bounds\n");

            // Add newest element to tally
            d_array[arrayAbleIndex] = d_array[arrayAbleIndex] + 1;

            // Find most common index
            if ((!d_MeasureLock) || (!d_enableLocking))
            {
              mostCommonIndex = FindMode(d_array, arraySize);//Intensive call
              mostCommonIndex = mostCommonIndex + myMin; // Unbias
              d_SavedIndex = mostCommonIndex; // Save as current best value

	    }
            else
              mostCommonIndex = d_SavedIndex;

            // Remove oldest sample from tally
            indexToBeRemoved = in[i] - myMin;
            if (d_array[indexToBeRemoved]>0)// startup case
              d_array[indexToBeRemoved] = d_array[indexToBeRemoved] - 1;


          // Output mode
          out[i] = mostCommonIndex;
        }

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace wifius */
} /* namespace gr */
