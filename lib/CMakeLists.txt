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
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})
list(APPEND wifius_sources
    measure_phases_impl.cc
    delay_sig_impl.cc
    mode_impl.cc
    correct_input_impl.cc
    int_to_message_impl.cc
    divide_by_message_impl.cc
    find_scale_factor_impl.cc
    blocker_impl.cc
    counter_signal_impl.cc )

set(wifius_sources "${wifius_sources}" PARENT_SCOPE)
if(NOT wifius_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT wifius_sources)

add_library(gnuradio-wifius SHARED ${wifius_sources})
target_link_libraries(gnuradio-wifius ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-wifius PROPERTIES DEFINE_SYMBOL "gnuradio_wifius_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-wifius PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
install(TARGETS gnuradio-wifius
    LIBRARY DESTINATION lib${LIB_SUFFIX} # .so/.dylib file
    ARCHIVE DESTINATION lib${LIB_SUFFIX} # .lib file
    RUNTIME DESTINATION bin              # .dll file
)

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_wifius_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_wifius.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_wifius.cc
)

add_executable(test-wifius ${test_wifius_sources})

target_link_libraries(
  test-wifius
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-wifius
)

GR_ADD_TEST(test_wifius test-wifius)
