#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Mar 22 17:37:27 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from sync_tx_hier import sync_tx_hier  # grc-generated hier_block
from sync_tx_hier2 import sync_tx_hier2  # grc-generated hier_block
import math
import numpy
import pmt
import sip
import time
import wifius


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_chooser_0_0_0 = variable_qtgui_chooser_0_0_0 = 1
        self.variable_qtgui_chooser_0_0 = variable_qtgui_chooser_0_0 = 1
        self.snapshots = snapshots = 4096
        self.samp_rate = samp_rate = 100000000/32
        self.pi = pi = 3.14159265359
        self.phase_c2 = phase_c2 = 0
        self.phase_c1 = phase_c1 = 0
        self.phase_c0 = phase_c0 = 0
        self.gain_rx = gain_rx = 20
        self.center_freq = center_freq = 2.4e9
        self.ant_cal_enable = ant_cal_enable = 1

        ##################################################
        # Blocks
        ##################################################
        _variable_qtgui_chooser_0_0_0_check_box = Qt.QCheckBox("TX OTA (Bottom) ")
        self._variable_qtgui_chooser_0_0_0_choices = {True: 0, False: 1}
        self._variable_qtgui_chooser_0_0_0_choices_inv = dict((v,k) for k,v in self._variable_qtgui_chooser_0_0_0_choices.iteritems())
        self._variable_qtgui_chooser_0_0_0_callback = lambda i: Qt.QMetaObject.invokeMethod(_variable_qtgui_chooser_0_0_0_check_box, "setChecked", Qt.Q_ARG("bool", self._variable_qtgui_chooser_0_0_0_choices_inv[i]))
        self._variable_qtgui_chooser_0_0_0_callback(self.variable_qtgui_chooser_0_0_0)
        _variable_qtgui_chooser_0_0_0_check_box.stateChanged.connect(lambda i: self.set_variable_qtgui_chooser_0_0_0(self._variable_qtgui_chooser_0_0_0_choices[bool(i)]))
        self.top_grid_layout.addWidget(_variable_qtgui_chooser_0_0_0_check_box, 1,0)
        _variable_qtgui_chooser_0_0_check_box = Qt.QCheckBox("TX Direct (Top)")
        self._variable_qtgui_chooser_0_0_choices = {True: 0, False: 1}
        self._variable_qtgui_chooser_0_0_choices_inv = dict((v,k) for k,v in self._variable_qtgui_chooser_0_0_choices.iteritems())
        self._variable_qtgui_chooser_0_0_callback = lambda i: Qt.QMetaObject.invokeMethod(_variable_qtgui_chooser_0_0_check_box, "setChecked", Qt.Q_ARG("bool", self._variable_qtgui_chooser_0_0_choices_inv[i]))
        self._variable_qtgui_chooser_0_0_callback(self.variable_qtgui_chooser_0_0)
        _variable_qtgui_chooser_0_0_check_box.stateChanged.connect(lambda i: self.set_variable_qtgui_chooser_0_0(self._variable_qtgui_chooser_0_0_choices[bool(i)]))
        self.top_grid_layout.addWidget(_variable_qtgui_chooser_0_0_check_box, 0,0)
        self._phase_c2_range = Range(-180, 180, 1, 0, 200)
        self._phase_c2_win = RangeWidget(self._phase_c2_range, self.set_phase_c2, "Phase Channel2", "counter_slider", float)
        self.top_layout.addWidget(self._phase_c2_win)
        self._phase_c1_range = Range(-180, 180, 1, 0, 200)
        self._phase_c1_win = RangeWidget(self._phase_c1_range, self.set_phase_c1, "Phase Channel1", "counter_slider", float)
        self.top_layout.addWidget(self._phase_c1_win)
        self._phase_c0_range = Range(-180, 180, 1, 0, 200)
        self._phase_c0_win = RangeWidget(self._phase_c0_range, self.set_phase_c0, "Phase Channel0", "counter_slider", float)
        self.top_layout.addWidget(self._phase_c0_win)
        _ant_cal_enable_check_box = Qt.QCheckBox("Enable Antenna Calibration")
        self._ant_cal_enable_choices = {True: 0, False: 1}
        self._ant_cal_enable_choices_inv = dict((v,k) for k,v in self._ant_cal_enable_choices.iteritems())
        self._ant_cal_enable_callback = lambda i: Qt.QMetaObject.invokeMethod(_ant_cal_enable_check_box, "setChecked", Qt.Q_ARG("bool", self._ant_cal_enable_choices_inv[i]))
        self._ant_cal_enable_callback(self.ant_cal_enable)
        _ant_cal_enable_check_box.stateChanged.connect(lambda i: self.set_ant_cal_enable(self._ant_cal_enable_choices[bool(i)]))
        self.top_grid_layout.addWidget(_ant_cal_enable_check_box, 1,4)
        self.wifius_gen_music_spectrum_vcvf_0 = wifius.gen_music_spectrum_vcvf(3, 1, -90, 90, 1, 0.5, 4096)
        self.wifius_antenna_array_calibration_cf_0 = wifius.antenna_array_calibration_cf(90, 0.5, 3, snapshots)
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
        	",".join(("addr0=192.168.40.2,addr1=192.168.50.2,addr2=192.168.60.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(3),
        	),
        )
        self.uhd_usrp_source_0_0.set_clock_source("external", 0)
        self.uhd_usrp_source_0_0.set_time_source("external", 0)
        self.uhd_usrp_source_0_0.set_clock_source("external", 1)
        self.uhd_usrp_source_0_0.set_time_source("external", 1)
        self.uhd_usrp_source_0_0.set_clock_source("mimo", 2)
        self.uhd_usrp_source_0_0.set_time_source("mimo", 2)
        self.uhd_usrp_source_0_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0_0.set_gain(gain_rx, 0)
        self.uhd_usrp_source_0_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0_0.set_center_freq(center_freq, 1)
        self.uhd_usrp_source_0_0.set_gain(gain_rx, 1)
        self.uhd_usrp_source_0_0.set_antenna("RX2", 1)
        self.uhd_usrp_source_0_0.set_center_freq(center_freq, 2)
        self.uhd_usrp_source_0_0.set_gain(gain_rx, 2)
        self.uhd_usrp_source_0_0.set_antenna("RX2", 2)
        self.sync_tx_hier_0_0 = sync_tx_hier(
            addr0="addr=192.168.30.2",
            cal_freq=10e3,
            center_freq=center_freq,
            gain_tx2=20,
            samp_rate=samp_rate,
            tone_type='Real',
        )
        self.sync_tx_hier2_0 = sync_tx_hier2(
            addr0="addr=192.168.20.2",
            cal_freq=10e3,
            center_freq=2.4e9,
            gain_tx2=20,
            samp_rate=samp_rate,
            tone_type='Real',
        )
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            180,
            -90,
            1.0,
            "Offset",
            "dB",
            "MuSIC Spectrum",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0.enable_autoscale(True)
        self.qtgui_vector_sink_f_0.enable_grid(True)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	300, #size
        	samp_rate, #samp_rate
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["RX1", "RX2", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_short,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        units = ["", "", "", "", "",
                 "", "", "", "", ""]
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, snapshots)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, snapshots)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, snapshots)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_multiply_const_vxx_0_0_0 = blocks.multiply_const_vcc((numpy.exp(-1j*phase_c2*pi/180), ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((numpy.exp(-1j*phase_c1*pi/180), ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((numpy.exp(-1j*phase_c0*pi/180), ))
        self.blocks_message_strobe_0_3 = blocks.message_strobe(pmt.from_double(ant_cal_enable), 1000)
        self.blocks_message_strobe_0_0 = blocks.message_strobe(pmt.from_double(variable_qtgui_chooser_0_0), 1000)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.from_double(variable_qtgui_chooser_0_0_0), 1000)
        self.blocks_complex_to_real_0_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.blocks_argmax_xx_0 = blocks.argmax_fs(180)
        self.blocks_add_const_vxx_0 = blocks.add_const_vss((-90, ))

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.sync_tx_hier2_0, 'Trigger'))    
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.sync_tx_hier_0_0, 'Trigger'))    
        self.msg_connect((self.blocks_message_strobe_0_3, 'strobe'), (self.wifius_antenna_array_calibration_cf_0, 'enable_hold'))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.qtgui_number_sink_0, 0))    
        self.connect((self.blocks_argmax_xx_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_argmax_xx_0, 1), (self.blocks_null_sink_0, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.blocks_complex_to_real_0_0_0, 0), (self.qtgui_time_sink_x_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.wifius_antenna_array_calibration_cf_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_complex_to_real_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_stream_to_vector_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.wifius_antenna_array_calibration_cf_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_complex_to_real_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.blocks_stream_to_vector_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0_0, 0), (self.wifius_antenna_array_calibration_cf_0, 2))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.wifius_gen_music_spectrum_vcvf_0, 2))    
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.wifius_gen_music_spectrum_vcvf_0, 3))    
        self.connect((self.blocks_stream_to_vector_0_0_0, 0), (self.wifius_gen_music_spectrum_vcvf_0, 4))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 1), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 2), (self.blocks_multiply_const_vxx_0_0_0, 0))    
        self.connect((self.wifius_antenna_array_calibration_cf_0, 0), (self.wifius_gen_music_spectrum_vcvf_0, 0))    
        self.connect((self.wifius_antenna_array_calibration_cf_0, 1), (self.wifius_gen_music_spectrum_vcvf_0, 1))    
        self.connect((self.wifius_gen_music_spectrum_vcvf_0, 0), (self.blocks_argmax_xx_0, 0))    
        self.connect((self.wifius_gen_music_spectrum_vcvf_0, 0), (self.qtgui_vector_sink_f_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_variable_qtgui_chooser_0_0_0(self):
        return self.variable_qtgui_chooser_0_0_0

    def set_variable_qtgui_chooser_0_0_0(self, variable_qtgui_chooser_0_0_0):
        self.variable_qtgui_chooser_0_0_0 = variable_qtgui_chooser_0_0_0
        self._variable_qtgui_chooser_0_0_0_callback(self.variable_qtgui_chooser_0_0_0)
        self.blocks_message_strobe_0.set_msg(pmt.from_double(self.variable_qtgui_chooser_0_0_0))

    def get_variable_qtgui_chooser_0_0(self):
        return self.variable_qtgui_chooser_0_0

    def set_variable_qtgui_chooser_0_0(self, variable_qtgui_chooser_0_0):
        self.variable_qtgui_chooser_0_0 = variable_qtgui_chooser_0_0
        self._variable_qtgui_chooser_0_0_callback(self.variable_qtgui_chooser_0_0)
        self.blocks_message_strobe_0_0.set_msg(pmt.from_double(self.variable_qtgui_chooser_0_0))

    def get_snapshots(self):
        return self.snapshots

    def set_snapshots(self, snapshots):
        self.snapshots = snapshots

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)
        self.sync_tx_hier_0_0.set_samp_rate(self.samp_rate)
        self.sync_tx_hier2_0.set_samp_rate(self.samp_rate)

    def get_pi(self):
        return self.pi

    def set_pi(self, pi):
        self.pi = pi
        self.blocks_multiply_const_vxx_0.set_k((numpy.exp(-1j*self.phase_c0*self.pi/180), ))
        self.blocks_multiply_const_vxx_0_0.set_k((numpy.exp(-1j*self.phase_c1*self.pi/180), ))
        self.blocks_multiply_const_vxx_0_0_0.set_k((numpy.exp(-1j*self.phase_c2*self.pi/180), ))

    def get_phase_c2(self):
        return self.phase_c2

    def set_phase_c2(self, phase_c2):
        self.phase_c2 = phase_c2
        self.blocks_multiply_const_vxx_0_0_0.set_k((numpy.exp(-1j*self.phase_c2*self.pi/180), ))

    def get_phase_c1(self):
        return self.phase_c1

    def set_phase_c1(self, phase_c1):
        self.phase_c1 = phase_c1
        self.blocks_multiply_const_vxx_0_0.set_k((numpy.exp(-1j*self.phase_c1*self.pi/180), ))

    def get_phase_c0(self):
        return self.phase_c0

    def set_phase_c0(self, phase_c0):
        self.phase_c0 = phase_c0
        self.blocks_multiply_const_vxx_0.set_k((numpy.exp(-1j*self.phase_c0*self.pi/180), ))

    def get_gain_rx(self):
        return self.gain_rx

    def set_gain_rx(self, gain_rx):
        self.gain_rx = gain_rx
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 0)
        	
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 1)
        	
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 2)
        	
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 3)
        	

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 1)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 2)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 3)
        self.sync_tx_hier_0_0.set_center_freq(self.center_freq)

    def get_ant_cal_enable(self):
        return self.ant_cal_enable

    def set_ant_cal_enable(self, ant_cal_enable):
        self.ant_cal_enable = ant_cal_enable
        self._ant_cal_enable_callback(self.ant_cal_enable)
        self.blocks_message_strobe_0_3.set_msg(pmt.from_double(self.ant_cal_enable))


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
