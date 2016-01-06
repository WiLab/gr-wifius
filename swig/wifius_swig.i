/* -*- c++ -*- */

#define WIFIUS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "wifius_swig_doc.i"

%{
#include "wifius/measure_phases.h"
#include "wifius/phase_offset.h"
#include "wifius/delay_sig.h"
#include "wifius/mode.h"
#include "wifius/correct_input.h"
#include "wifius/int_to_message.h"
#include "wifius/divide_by_message.h"
#include "wifius/find_scale_factor.h"
%}


%include "wifius/measure_phases.h"
GR_SWIG_BLOCK_MAGIC2(wifius, measure_phases);
%include "wifius/phase_offset.h"
GR_SWIG_BLOCK_MAGIC2(wifius, phase_offset);
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
