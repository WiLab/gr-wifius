# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Phase Align
# Author: Travis Collins
# Description: Align Phases of N Input Signals
# Generated: Thu Feb 25 15:20:56 2016
##################################################

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import pmt
import wifius

def gen_sig_io(num_elements):
    # Dynamically create types for signature
    io = []
    for i in range(num_elements):
        io.append(gr.sizeof_gr_complex*1)
    return io

class phase_align_hier(gr.hier_block2):

    def __init__(self, update_period=32, window=1024, step_size=0.001, num_ports=2):
        gr.hier_block2.__init__(
            self, "Phase Align",
            gr.io_signaturev(num_ports, num_ports, gen_sig_io(num_ports)),
            gr.io_signaturev(num_ports, num_ports, gen_sig_io(num_ports)),
        )
        self.message_port_register_hier_in("Trigger")

        ##################################################
        # Parameters
        ##################################################
        self.update_period = update_period
        self.window = window
        self.step_size = step_size
        self.num_ports = num_ports

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################

        # Const block for reference signal to do nothing
        self.blocks_add_const_vxx_0 = blocks.add_const_vcc((0, ))
        self.connect((self, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self, 0))

        for p in range(num_ports-1):
            # Create PC object
            object_name_pc = 'wifius_phase_correct_vci_'+str(p)
            setattr(self, object_name_pc, wifius.phase_correct_vci(1024, samp_rate, window, step_size, update_period, False))

            # Add Stream To Vector For Ref
            object_name_vr = 'blocks_stream_to_vector_a_'+str(p)
            setattr(self, object_name_vr, blocks.stream_to_vector(gr.sizeof_gr_complex*1, window))

            # Add Stream To Vector For Next Signal
            object_name_sv = 'blocks_stream_to_vector_b_'+str(p)
            setattr(self, object_name_sv, blocks.stream_to_vector(gr.sizeof_gr_complex*1, window))

            # Add Vector To Stream For Output of PC
            object_name_vs = 'blocks_vector_to_stream_'+str(p)
            setattr(self, object_name_vs, blocks.vector_to_stream(gr.sizeof_gr_complex*1, window))

            # Make Connections
            self.connect((self, 0),   (getattr(self,object_name_vr), 0))
            self.connect((self, p+1), (getattr(self,object_name_sv), 0))

            self.connect((getattr(self,object_name_vr), 0), (getattr(self,object_name_pc), 0))
            self.connect((getattr(self,object_name_sv), 0), (getattr(self,object_name_pc), 1))

            self.connect((getattr(self,object_name_pc), 0), (getattr(self,object_name_vs), 0))

            self.connect((getattr(self,object_name_vs), 0), (self, p+1))

            self.msg_connect((self, 'Trigger'), (getattr(self,object_name_pc), 'set_enable_sync'))


    def get_update_period(self):
        return self.update_period

    def set_update_period(self, update_period):
        self.update_period = update_period

    def get_window(self):
        return self.window

    def set_window(self, window):
        self.window = window

    def get_step_size(self):
        return self.step_size

    def set_step_size(self, step_size):
        self.step_size = step_size

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
