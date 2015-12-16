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

#ifndef INCLUDED_WIFIUS_MEASURE_PHASES_IMPL_H
#define INCLUDED_WIFIUS_MEASURE_PHASES_IMPL_H

#include <wifius/measure_phases.h>

namespace gr {
  namespace wifius {

    class measure_phases_impl : public measure_phases
    {
     private:
      size_t d_vlen;
      float d_SampleRate;
      float d_ToneFreq;
      float d_SamplesPerRadian;
      int d_SamplesNeeded;
      float d_SamplesPerPeriod;
      int *d_Delays;
      bool d_HaveBeenDelayed;
      int d_lastUpdate;
      int d_UpdatePeriod;

     public:
      // Additional prototypes
      int GetPeak(float *signal, int &start, int &signalLength);
      float GetPhaseDiff(int &distance);
      int* DetermineCasualOffsets(int *positions, int &numInputs);

      // Typical Declarations for GR blocks
      measure_phases_impl(float SampleRate, float CalibrationToneFrequency, int UpdatePeriod, size_t vlen);
      ~measure_phases_impl();

      // Where all the action really happens
      int work(int noutput_items,
		       gr_vector_const_void_star &input_items,
		       gr_vector_void_star &output_items);
    };

  } // namespace wifius
} // namespace gr

#endif /* INCLUDED_WIFIUS_MEASURE_PHASES_IMPL_H */
