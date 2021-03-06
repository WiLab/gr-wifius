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

########################################################################
# Include python install macros
########################################################################
include(GrPython)
if(NOT PYTHONINTERP_FOUND)
    return()
endif()

########################################################################
# Install python sources
########################################################################
GR_PYTHON_INSTALL(
    FILES
    __init__.py
    phase_align_hier.py
    music_spectrum_hier_gui.py
    doa_txs.py
    selector_control.py DESTINATION ${GR_PYTHON_DIR}/wifius
)


########################################################################
# Handle the unit tests
########################################################################
include(GrTest)

set(GR_TEST_TARGET_DEPS gnuradio-wifius)
set(GR_TEST_PYTHON_DIRS ${CMAKE_BINARY_DIR}/swig)
GR_ADD_TEST(qa_measure_phases ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_measure_phases.py)
GR_ADD_TEST(qa_delay_sig ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_delay_sig.py)
GR_ADD_TEST(qa_mode ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_mode.py)
GR_ADD_TEST(qa_correct_input ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_correct_input.py)
GR_ADD_TEST(qa_int_to_message ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_int_to_message.py)
GR_ADD_TEST(qa_divide_by_message ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_divide_by_message.py)
GR_ADD_TEST(qa_find_scale_factor ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_find_scale_factor.py)
GR_ADD_TEST(qa_blocker ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_blocker.py)
GR_ADD_TEST(qa_counter_signal ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_counter_signal.py)
GR_ADD_TEST(qa_shift_and_measure ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_shift_and_measure.py)
GR_ADD_TEST(qa_phase_correct_vci ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_phase_correct_vci.py)
#GR_ADD_TEST(qa_doa_music_vcvf ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_doa_music_vcvf.py)
GR_ADD_TEST(qa_StreamsToRxx ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_StreamsToRxx.py)
GR_ADD_TEST(qa_gen_music_spectrum_vcvf ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_gen_music_spectrum_vcvf.py)
GR_ADD_TEST(qa_antenna_array_calibration_cf ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_antenna_array_calibration_cf.py)
GR_ADD_TEST(qa_selector_control ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_selector_control.py)
GR_ADD_TEST(qa_mux_gate ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/qa_mux_gate.py)
