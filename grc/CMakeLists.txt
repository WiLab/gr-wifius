# Copyright 2011 Free Software Foundation, Inc.
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
install(FILES
    wifius_measure_phases.xml
    wifius_delay_sig.xml
    wifius_mode.xml
    wifius_correct_input.xml
    wifius_int_to_message.xml
    wifius_divide_by_message.xml
    wifius_find_scale_factor.xml
    wifius_blocker.xml
    wifius_counter_signal.xml
    wifius_shift_and_measure.xml
    wifius_phase_correct_vci.xml DESTINATION share/gnuradio/grc/blocks
)
