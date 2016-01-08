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
