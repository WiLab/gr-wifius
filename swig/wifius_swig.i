/* -*- c++ -*- */

#define WIFIUS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "wifius_swig_doc.i"

%{
#include "wifius/measure_phases.h"
#include "wifius/delay_sig.h"
#include "wifius/mode.h"
#include "wifius/correct_input.h"
#include "wifius/int_to_message.h"
#include "wifius/divide_by_message.h"
#include "wifius/find_scale_factor.h"
#include "wifius/blocker.h"
#include "wifius/counter_signal.h"
#include "wifius/shift_and_measure.h"
#include "wifius/phase_correct_vci.h"
#include "wifius/doa_music_vcvf.h"
#include "wifius/StreamsToRxx.h"
#include "wifius/gen_music_spectrum_vcvf.h"
#include "wifius/antenna_array_calibration_cf.h"
#include "wifius/mux_gate.h"
//#include "wifius/selector_control.h"
//#include "wifius/antenna_compensator.h"
%}


%include "wifius/measure_phases.h"
GR_SWIG_BLOCK_MAGIC2(wifius, measure_phases);

%include "wifius/delay_sig.h"
GR_SWIG_BLOCK_MAGIC2(wifius, delay_sig);
%include "wifius/mode.h"
GR_SWIG_BLOCK_MAGIC2(wifius, mode);

%include "wifius/correct_input.h"
GR_SWIG_BLOCK_MAGIC2(wifius, correct_input);

%include "wifius/int_to_message.h"
GR_SWIG_BLOCK_MAGIC2(wifius, int_to_message);
%include "wifius/divide_by_message.h"
GR_SWIG_BLOCK_MAGIC2(wifius, divide_by_message);

%include "wifius/find_scale_factor.h"
GR_SWIG_BLOCK_MAGIC2(wifius, find_scale_factor);
%include "wifius/blocker.h"
GR_SWIG_BLOCK_MAGIC2(wifius, blocker);
%include "wifius/counter_signal.h"
GR_SWIG_BLOCK_MAGIC2(wifius, counter_signal);
%include "wifius/shift_and_measure.h"
GR_SWIG_BLOCK_MAGIC2(wifius, shift_and_measure);
%include "wifius/phase_correct_vci.h"
GR_SWIG_BLOCK_MAGIC2(wifius, phase_correct_vci);
//%include "wifius/antenna_compensator.h"
//GR_SWIG_BLOCK_MAGIC2(wifius, antenna_compensator);
%include "wifius/doa_music_vcvf.h"
GR_SWIG_BLOCK_MAGIC2(wifius, doa_music_vcvf);
%include "wifius/StreamsToRxx.h"
GR_SWIG_BLOCK_MAGIC2(wifius, StreamsToRxx);
%include "wifius/gen_music_spectrum_vcvf.h"
GR_SWIG_BLOCK_MAGIC2(wifius, gen_music_spectrum_vcvf);
%include "wifius/antenna_array_calibration_cf.h"
GR_SWIG_BLOCK_MAGIC2(wifius, antenna_array_calibration_cf);
//%include "wifius/selector_control.h"
//GR_SWIG_BLOCK_MAGIC2(wifius, selector_control);
%include "wifius/mux_gate.h"
GR_SWIG_BLOCK_MAGIC2(wifius, mux_gate);
