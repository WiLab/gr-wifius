/* -*- c++ -*- */

#define WIFIUS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "wifius_swig_doc.i"

%{
#include "wifius/measure_phases.h"
#include "wifius/phase_offset.h"
#include "wifius/delay_sig.h"
%}


%include "wifius/measure_phases.h"
GR_SWIG_BLOCK_MAGIC2(wifius, measure_phases);
%include "wifius/phase_offset.h"
GR_SWIG_BLOCK_MAGIC2(wifius, phase_offset);
%include "wifius/delay_sig.h"
GR_SWIG_BLOCK_MAGIC2(wifius, delay_sig);
