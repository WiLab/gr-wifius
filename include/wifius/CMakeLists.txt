# Copyright 2011,2012 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Install public header files
########################################################################
install(FILES
    api.h
    measure_phases.h
    delay_sig.h
    mode.h
    correct_input.h
    int_to_message.h
    divide_by_message.h
    find_scale_factor.h
    blocker.h
    counter_signal.h
    shift_and_measure.h
    phase_correct_vci.h
    #antenna_compensator.h
    doa_music_vcvf.h
    StreamsToRxx.h
    gen_music_spectrum_vcvf.h
    antenna_array_calibration_cf.h
    mux_gate.h DESTINATION include/wifius
)
