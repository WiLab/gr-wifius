#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Calibration Example
# Author: Travis Collins
# Description: WiFiUS Project
# Generated: Tue Jan  5 15:51:10 2016
##################################################

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from correct_gains_hier import correct_gains_hier  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from measure_phases import measure_phases  # grc-generated hier_block
from optparse import OptionParser
import time


class calibration_example_tofile(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Calibration Example")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1024000*2
        self.gain_rx = gain_rx = 0
        self.center_freq = center_freq = 2.4e9
        self.cal_freq = cal_freq = 1000

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
        	",".join(("addr0=192.168.30.2,addr1=192.168.70.2,addr2=192.168.20.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(3),
        	),
        )
        self.uhd_usrp_source_0_0.set_clock_source("external", 0)
        self.uhd_usrp_source_0_0.set_time_source("external", 0)
        self.uhd_usrp_source_0_0.set_clock_source("external", 1)
        self.uhd_usrp_source_0_0.set_time_source("external", 1)
        self.uhd_usrp_source_0_0.set_clock_source("external", 2)
        self.uhd_usrp_source_0_0.set_time_source("external", 2)
        self.uhd_usrp_source_0_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0_0.set_gain(gain_rx, 0)
        self.uhd_usrp_source_0_0.set_center_freq(center_freq, 1)
        self.uhd_usrp_source_0_0.set_gain(gain_rx, 1)
        self.uhd_usrp_source_0_0.set_center_freq(center_freq, 2)
        self.uhd_usrp_source_0_0.set_gain(gain_rx, 2)
        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
        	",".join(("addr=192.168.10.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_sink_0_0.set_gain(10, 0)
        self.measure_phases_0 = measure_phases(
            cal_tone_freq=cal_freq,
            memSize=1024,
            samp_rate=samp_rate,
            skip=1024000*10,
            updatePeriod=1000,
        )
        self.correct_gains_hier_0 = correct_gains_hier(
            cal_tone_freq=cal_freq,
            samp_rate=samp_rate,
        )
        self.blocks_head_0_1 = blocks.head(gr.sizeof_gr_complex*1, 10000000)
        self.blocks_head_0_0 = blocks.head(gr.sizeof_gr_complex*1, 10000000)
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, 10000000)
        self.blocks_file_sink_0_1 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/travis/Dropbox/PHD/WiFiUS/doa/gnuradio/gr-wifius/data/channel2_complex.bin", False)
        self.blocks_file_sink_0_1.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/travis/Dropbox/PHD/WiFiUS/doa/gnuradio/gr-wifius/data/channel1_complex.bin", False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, "/home/travis/Dropbox/PHD/WiFiUS/doa/gnuradio/gr-wifius/data/channel0_complex.bin", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, cal_freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.uhd_usrp_sink_0_0, 0))    
        self.connect((self.blocks_head_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_head_0_0, 0), (self.blocks_file_sink_0_0, 0))    
        self.connect((self.blocks_head_0_1, 0), (self.blocks_file_sink_0_1, 0))    
        self.connect((self.correct_gains_hier_0, 0), (self.measure_phases_0, 0))    
        self.connect((self.correct_gains_hier_0, 1), (self.measure_phases_0, 1))    
        self.connect((self.correct_gains_hier_0, 2), (self.measure_phases_0, 2))    
        self.connect((self.measure_phases_0, 0), (self.blocks_head_0, 0))    
        self.connect((self.measure_phases_0, 1), (self.blocks_head_0_0, 0))    
        self.connect((self.measure_phases_0, 2), (self.blocks_head_0_1, 0))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.correct_gains_hier_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 1), (self.correct_gains_hier_0, 1))    
        self.connect((self.uhd_usrp_source_0_0, 2), (self.correct_gains_hier_0, 2))    


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.correct_gains_hier_0.set_samp_rate(self.samp_rate)
        self.measure_phases_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)

    def get_gain_rx(self):
        return self.gain_rx

    def set_gain_rx(self, gain_rx):
        self.gain_rx = gain_rx
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 0)
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 1)
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 2)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.uhd_usrp_sink_0_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 1)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 2)

    def get_cal_freq(self):
        return self.cal_freq

    def set_cal_freq(self, cal_freq):
        self.cal_freq = cal_freq
        self.analog_sig_source_x_0.set_frequency(self.cal_freq)
        self.correct_gains_hier_0.set_cal_tone_freq(self.cal_freq)
        self.measure_phases_0.set_cal_tone_freq(self.cal_freq)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = calibration_example_tofile()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()
