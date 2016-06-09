# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: DoA Transmitters
# Author: Travis Collins
# Generated: Wed Jun  8 19:24:03 2016
##################################################

from gnuradio import analog
from gnuradio import gr
from gnuradio import uhd
from gnuradio.filter import firdes
import pmt
import time
import wifius


class doa_txs(gr.hier_block2):

    def __init__(self, samp_rate=0, center_freq=2.4e9, usrp_address="addr0=192.168.10.1"):
        gr.hier_block2.__init__(
            self, "DoA Transmitters",
            gr.io_signature(0, 0, 0),
            gr.io_signature(0, 0, 0),
        )
        self.message_port_register_hier_in("Transmitter")



        ##################################################
        # Parameters
        ##################################################
        self.samp_rate = samp_rate
        self.center_freq = center_freq
        self.usrp_address = usrp_address
        self.num_transmitters = len(usrp_address.split())

        ##################################################
        # Blocks
        ##################################################
        self.wifius_mux_gate_0 = wifius.mux_gate(self.num_transmitters, -1)
        n = 0
        for tx in usrp_address.split():

            # Set Parameters for USRP
            tmp = uhd.usrp_sink(",".join((tx, "")),uhd.stream_args(cpu_format="fc32",channels=range(1),),)
            tmp.set_samp_rate(samp_rate)
            tmp.set_center_freq(center_freq, 0)
            tmp.set_gain(0, 0)
            # add to self
            object_name_sv = 'uhd_usrp_sink_0_'+str(n)
            setattr(self, object_name_sv, tmp )
            # Connect
            self.connect((self.wifius_mux_gate_0, 0), (getattr(self,object_name_sv), 0)  )

        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self, 'Transmitter'), (self.wifius_mux_gate_0, 'select_output'))
        self.connect((self.analog_sig_source_x_0, 0), (self.wifius_mux_gate_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    # def set_samp_rate(self, samp_rate):
    #     self.samp_rate = samp_rate
    #     self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
    #     self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)
    #     self.uhd_usrp_sink_0_1.set_samp_rate(self.samp_rate)
    #     self.uhd_usrp_sink_0_1_0.set_samp_rate(self.samp_rate)

    def get_center_freq(self):
        return self.center_freq

    # def set_center_freq(self, center_freq):
    #     self.center_freq = center_freq
    #     self.uhd_usrp_sink_0.set_center_freq(self.center_freq, 0)
    #     self.uhd_usrp_sink_0_1.set_center_freq(self.center_freq, 0)
    #     self.uhd_usrp_sink_0_1_0.set_center_freq(self.center_freq, 0)

    def get_usrp_address(self):
        return self.usrp_address

    def set_usrp_address(self, usrp_address):
        self.usrp_address = usrp_address
