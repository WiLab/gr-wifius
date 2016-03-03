#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Calibration Example
# Author: Travis Collins
# Description: WiFiUS Project
# Generated: Wed Mar  2 18:27:02 2016
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
from doa_ants_hier import doa_ants_hier  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from phase_align_hier import phase_align_hier  # grc-generated hier_block
from real_time_scope_hier import real_time_scope_hier  # grc-generated hier_block
from save_data_hier import save_data_hier  # grc-generated hier_block
from sync_tx_hier import sync_tx_hier  # grc-generated hier_block
from target_tx_hier import target_tx_hier  # grc-generated hier_block
import ConfigParser
import math
import numpy
import pmt
import sip
import time
import wifius


class calibration_example_gui(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Calibration Example")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Calibration Example")
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

        self.settings = Qt.QSettings("GNU Radio", "calibration_example_gui")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.antenna_spacing_inches = antenna_spacing_inches = 2.4
        self.speed_of_light = speed_of_light = 299792458
        self.gain_rx_array = gain_rx_array = 3
        self.antenna_spacing = antenna_spacing = antenna_spacing_inches*0.0254
        self.window = window = 1024
        self.variable_qtgui_chooser_0_1_1 = variable_qtgui_chooser_0_1_1 = 1
        self.variable_qtgui_chooser_0_0 = variable_qtgui_chooser_0_0 = 0
        self.sync = sync = pmt.PMT_F
        self._samples_to_save_config = ConfigParser.ConfigParser()
        self._samples_to_save_config.read("/home/travis/Dropbox/PHD/WiFiUS/doa/gnuradio/gr-matlab/config.gr")
        try: samples_to_save = self._samples_to_save_config.getfloat("rx", "samples_to_save")
        except: samples_to_save = 2**18
        self.samples_to_save = samples_to_save
        self.samp_rate = samp_rate = 100000000/64
        self.pi = pi = 3.14159265359
        self.phase_c3 = phase_c3 = 0
        self.phase_c2 = phase_c2 = 0
        self.phase_c1 = phase_c1 = 0
        self.phase_c0 = phase_c0 = 0
        self.offset = offset = 0
        self.label2 = label2 = "Check To Enable"
        self.label = label = "Check To Enable"
        self.gain_tx2 = gain_tx2 = 20
        self.gain_tx1 = gain_tx1 = 20
        self.gain_rx = gain_rx = gain_rx_array
        self.distant_tx_target = distant_tx_target = 1
        self.distant_tx = distant_tx = 1
        self.center_freq = center_freq = speed_of_light/(2*antenna_spacing)
        self.cal_freq = cal_freq = 10000
        self.ant_cal_enable = ant_cal_enable = 1

        ##################################################
        # Blocks
        ##################################################
        _variable_qtgui_chooser_0_1_1_check_box = Qt.QCheckBox("Trigger Data Save")
        self._variable_qtgui_chooser_0_1_1_choices = {True: 0, False: 1}
        self._variable_qtgui_chooser_0_1_1_choices_inv = dict((v,k) for k,v in self._variable_qtgui_chooser_0_1_1_choices.iteritems())
        self._variable_qtgui_chooser_0_1_1_callback = lambda i: Qt.QMetaObject.invokeMethod(_variable_qtgui_chooser_0_1_1_check_box, "setChecked", Qt.Q_ARG("bool", self._variable_qtgui_chooser_0_1_1_choices_inv[i]))
        self._variable_qtgui_chooser_0_1_1_callback(self.variable_qtgui_chooser_0_1_1)
        _variable_qtgui_chooser_0_1_1_check_box.stateChanged.connect(lambda i: self.set_variable_qtgui_chooser_0_1_1(self._variable_qtgui_chooser_0_1_1_choices[bool(i)]))
        self.top_grid_layout.addWidget(_variable_qtgui_chooser_0_1_1_check_box, 4,0)
        _variable_qtgui_chooser_0_0_check_box = Qt.QCheckBox("Connected Sync Tx")
        self._variable_qtgui_chooser_0_0_choices = {True: 0, False: 1}
        self._variable_qtgui_chooser_0_0_choices_inv = dict((v,k) for k,v in self._variable_qtgui_chooser_0_0_choices.iteritems())
        self._variable_qtgui_chooser_0_0_callback = lambda i: Qt.QMetaObject.invokeMethod(_variable_qtgui_chooser_0_0_check_box, "setChecked", Qt.Q_ARG("bool", self._variable_qtgui_chooser_0_0_choices_inv[i]))
        self._variable_qtgui_chooser_0_0_callback(self.variable_qtgui_chooser_0_0)
        _variable_qtgui_chooser_0_0_check_box.stateChanged.connect(lambda i: self.set_variable_qtgui_chooser_0_0(self._variable_qtgui_chooser_0_0_choices[bool(i)]))
        self.top_grid_layout.addWidget(_variable_qtgui_chooser_0_0_check_box, 3,0)
        self.tab = Qt.QTabWidget()
        self.tab_widget_0 = Qt.QWidget()
        self.tab_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_0)
        self.tab_grid_layout_0 = Qt.QGridLayout()
        self.tab_layout_0.addLayout(self.tab_grid_layout_0)
        self.tab.addTab(self.tab_widget_0, "Input")
        self.tab_widget_1 = Qt.QWidget()
        self.tab_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_1)
        self.tab_grid_layout_1 = Qt.QGridLayout()
        self.tab_layout_1.addLayout(self.tab_grid_layout_1)
        self.tab.addTab(self.tab_widget_1, "Post Phase Correct")
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, "Angle of Arrival")
        self.tab_widget_3 = Qt.QWidget()
        self.tab_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_3)
        self.tab_grid_layout_3 = Qt.QGridLayout()
        self.tab_layout_3.addLayout(self.tab_grid_layout_3)
        self.tab.addTab(self.tab_widget_3, "MuSIC Spectrum")
        self.top_layout.addWidget(self.tab)
        _sync_check_box = Qt.QCheckBox("Enable Sync Adaption")
        self._sync_choices = {True: pmt.PMT_T, False: pmt.PMT_F}
        self._sync_choices_inv = dict((v,k) for k,v in self._sync_choices.iteritems())
        self._sync_callback = lambda i: Qt.QMetaObject.invokeMethod(_sync_check_box, "setChecked", Qt.Q_ARG("bool", self._sync_choices_inv[i]))
        self._sync_callback(self.sync)
        _sync_check_box.stateChanged.connect(lambda i: self.set_sync(self._sync_choices[bool(i)]))
        self.top_grid_layout.addWidget(_sync_check_box, 1,1)
        self._phase_c3_range = Range(-180, 180, 1, 0, 200)
        self._phase_c3_win = RangeWidget(self._phase_c3_range, self.set_phase_c3, "Phase Channel3", "counter_slider", float)
        self.top_layout.addWidget(self._phase_c3_win)
        self._phase_c2_range = Range(-180, 180, 1, 0, 200)
        self._phase_c2_win = RangeWidget(self._phase_c2_range, self.set_phase_c2, "Phase Channel2", "counter_slider", float)
        self.top_layout.addWidget(self._phase_c2_win)
        self._phase_c1_range = Range(-180, 180, 1, 0, 200)
        self._phase_c1_win = RangeWidget(self._phase_c1_range, self.set_phase_c1, "Phase Channel1", "counter_slider", float)
        self.top_layout.addWidget(self._phase_c1_win)
        self._phase_c0_range = Range(-180, 180, 1, 0, 200)
        self._phase_c0_win = RangeWidget(self._phase_c0_range, self.set_phase_c0, "Phase Channel0", "counter_slider", float)
        self.top_layout.addWidget(self._phase_c0_win)
        self._gain_tx2_range = Range(0, 30, 1, 20, 200)
        self._gain_tx2_win = RangeWidget(self._gain_tx2_range, self.set_gain_tx2, "Gain DRTX 2", "counter", float)
        self.top_grid_layout.addWidget(self._gain_tx2_win, 4,1)
        self._gain_tx1_range = Range(0, 30, 1, 20, 200)
        self._gain_tx1_win = RangeWidget(self._gain_tx1_range, self.set_gain_tx1, "Gain DRTX 1", "counter", float)
        self.top_grid_layout.addWidget(self._gain_tx1_win, 3,1)
        _distant_tx_target_check_box = Qt.QCheckBox("Distant TX Target")
        self._distant_tx_target_choices = {True: 0, False: 1}
        self._distant_tx_target_choices_inv = dict((v,k) for k,v in self._distant_tx_target_choices.iteritems())
        self._distant_tx_target_callback = lambda i: Qt.QMetaObject.invokeMethod(_distant_tx_target_check_box, "setChecked", Qt.Q_ARG("bool", self._distant_tx_target_choices_inv[i]))
        self._distant_tx_target_callback(self.distant_tx_target)
        _distant_tx_target_check_box.stateChanged.connect(lambda i: self.set_distant_tx_target(self._distant_tx_target_choices[bool(i)]))
        self.top_grid_layout.addWidget(_distant_tx_target_check_box, 2,0)
        _distant_tx_check_box = Qt.QCheckBox("Distant TX Ref")
        self._distant_tx_choices = {True: 0, False: 1}
        self._distant_tx_choices_inv = dict((v,k) for k,v in self._distant_tx_choices.iteritems())
        self._distant_tx_callback = lambda i: Qt.QMetaObject.invokeMethod(_distant_tx_check_box, "setChecked", Qt.Q_ARG("bool", self._distant_tx_choices_inv[i]))
        self._distant_tx_callback(self.distant_tx)
        _distant_tx_check_box.stateChanged.connect(lambda i: self.set_distant_tx(self._distant_tx_choices[bool(i)]))
        self.top_grid_layout.addWidget(_distant_tx_check_box, 1,0)
        _ant_cal_enable_check_box = Qt.QCheckBox("Enable Antenna Calibration")
        self._ant_cal_enable_choices = {True: 0, False: 1}
        self._ant_cal_enable_choices_inv = dict((v,k) for k,v in self._ant_cal_enable_choices.iteritems())
        self._ant_cal_enable_callback = lambda i: Qt.QMetaObject.invokeMethod(_ant_cal_enable_check_box, "setChecked", Qt.Q_ARG("bool", self._ant_cal_enable_choices_inv[i]))
        self._ant_cal_enable_callback(self.ant_cal_enable)
        _ant_cal_enable_check_box.stateChanged.connect(lambda i: self.set_ant_cal_enable(self._ant_cal_enable_choices[bool(i)]))
        self.top_grid_layout.addWidget(_ant_cal_enable_check_box, 1,4)
        self.wifius_gen_music_spectrum_vcvf_0 = wifius.gen_music_spectrum_vcvf(4, 1, -90, 90, 1, 0.5, 4096)
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
        	",".join(("addr0=192.168.20.2,addr1=192.168.30.2,addr2=192.168.40.2,addr3=192.168.50.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(4),
        	),
        )
        self.uhd_usrp_source_0_0.set_clock_source("external", 0)
        self.uhd_usrp_source_0_0.set_time_source("external", 0)
        self.uhd_usrp_source_0_0.set_clock_source("external", 1)
        self.uhd_usrp_source_0_0.set_time_source("external", 1)
        self.uhd_usrp_source_0_0.set_clock_source("external", 2)
        self.uhd_usrp_source_0_0.set_time_source("external", 2)
        self.uhd_usrp_source_0_0.set_clock_source("external", 3)
        self.uhd_usrp_source_0_0.set_time_source("external", 3)
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
        self.uhd_usrp_source_0_0.set_center_freq(center_freq, 3)
        self.uhd_usrp_source_0_0.set_gain(gain_rx, 3)
        self.uhd_usrp_source_0_0.set_antenna("RX2", 3)
        self.target_tx_hier_0_0 = target_tx_hier(
            addr0="addr=192.168.90.2",
            cal_freq=10e3,
            center_freq=center_freq,
            gain_tx2=gain_tx1,
            samp_rate=samp_rate,
            tone_type="Real",
        )
        self.target_tx_hier_0 = target_tx_hier(
            addr0="addr=192.168.80.2",
            cal_freq=10e3,
            center_freq=center_freq,
            gain_tx2=gain_tx2,
            samp_rate=samp_rate,
            tone_type="Real",
        )
        self.sync_tx_hier_0 = sync_tx_hier(
            addr0="addr=192.168.60.2",
            cal_freq=10e3,
            center_freq=center_freq,
            gain_tx2=10,
            samp_rate=samp_rate,
            tone_type="Complex",
        )
        self.save_data_hier_0 = save_data_hier(
            keep=1,
            samples=2**16,
            skips=2**16,
            vec_size=64,
        )
        self.real_time_scope_hier_0_0_0_0 = real_time_scope_hier(
            npoints=3000,
            samp_rate=samp_rate,
        )
        self.tab_layout_0.addWidget(self.real_time_scope_hier_0_0_0_0)
        self.real_time_scope_hier_0_0_0 = real_time_scope_hier(
            npoints=3000,
            samp_rate=samp_rate,
        )
        self.tab_layout_1.addWidget(self.real_time_scope_hier_0_0_0)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            180,
            -90,
            1.0,
            "Angle",
            "dB",
            "",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-10, 5)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
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
        self.tab_layout_3.addWidget(self._qtgui_vector_sink_f_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	16, #size
        	samp_rate, #samp_rate
        	"Angle of Arrival", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-90, 90)
        
        self.qtgui_time_sink_x_0.set_y_label("Angle", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, False)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [0, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
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
        self.tab_layout_2.addWidget(self._qtgui_time_sink_x_0_win)
        self.phase_align_hier_0 = phase_align_hier(
            update_period=32,
            window=window,
            step_size=0.001,
        )
        self._offset_range = Range(-90, 90, 1, 0, 10)
        self._offset_win = RangeWidget(self._offset_range, self.set_offset, "Bias Angle", "counter", float)
        self.top_grid_layout.addWidget(self._offset_win, 2,1)
        self._label2_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._label2_formatter = None
        else:
          self._label2_formatter = lambda x: x
        
        self._label2_tool_bar.addWidget(Qt.QLabel("Algorithm  Control"+": "))
        self._label2_label = Qt.QLabel(str(self._label2_formatter(self.label2)))
        self._label2_tool_bar.addWidget(self._label2_label)
        self.top_grid_layout.addWidget(self._label2_tool_bar, 0,1)
          
        self._label_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._label_formatter = None
        else:
          self._label_formatter = lambda x: x
        
        self._label_tool_bar.addWidget(Qt.QLabel("Transmitter Control"+": "))
        self._label_label = Qt.QLabel(str(self._label_formatter(self.label)))
        self._label_tool_bar.addWidget(self._label_label)
        self.top_grid_layout.addWidget(self._label_tool_bar, 0,0)
          
        self._gain_rx_array_range = Range(0, 30, 1, 3, 200)
        self._gain_rx_array_win = RangeWidget(self._gain_rx_array_range, self.set_gain_rx_array, "Gain RX Array", "counter", float)
        self.top_grid_layout.addWidget(self._gain_rx_array_win, 5,1)
        self.doa_ants_hier_0 = doa_ants_hier(
            snapshots=4096,
            true_angle=90-33,
        )
        self.blocks_multiply_const_vxx_0_2 = blocks.multiply_const_vcc((numpy.exp(-1j*2*pi*numpy.sin(phase_c3*pi/180)), ))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vcc((numpy.exp(-1j*2*pi*numpy.sin(phase_c2*pi/180)), ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((numpy.exp(-1j*2*pi*numpy.sin(phase_c1*pi/180)), ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((numpy.exp(-1j*2*pi*numpy.sin(phase_c0*pi/180)), ))
        self.blocks_message_strobe_0_3 = blocks.message_strobe(pmt.from_double(ant_cal_enable), 1000)
        self.blocks_message_strobe_0_2_0 = blocks.message_strobe(pmt.from_double(distant_tx_target), 1000)
        self.blocks_message_strobe_0_2 = blocks.message_strobe(pmt.from_double(distant_tx), 1000)
        self.blocks_message_strobe_0_1 = blocks.message_strobe(sync, 1000)
        self.blocks_message_strobe_0_0 = blocks.message_strobe(pmt.from_double(variable_qtgui_chooser_0_1_1), 1000)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.from_double(variable_qtgui_chooser_0_0), 1000)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.sync_tx_hier_0, 'Trigger'))    
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.save_data_hier_0, 'Trigger'))    
        self.msg_connect((self.blocks_message_strobe_0_1, 'strobe'), (self.phase_align_hier_0, 'Trigger'))    
        self.msg_connect((self.blocks_message_strobe_0_2, 'strobe'), (self.target_tx_hier_0, 'Trigger'))    
        self.msg_connect((self.blocks_message_strobe_0_2_0, 'strobe'), (self.target_tx_hier_0_0, 'Trigger'))    
        self.msg_connect((self.blocks_message_strobe_0_3, 'strobe'), (self.doa_ants_hier_0, 'Trigger'))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.doa_ants_hier_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.real_time_scope_hier_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.save_data_hier_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.wifius_gen_music_spectrum_vcvf_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.doa_ants_hier_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.real_time_scope_hier_0_0_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.save_data_hier_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.wifius_gen_music_spectrum_vcvf_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.doa_ants_hier_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.real_time_scope_hier_0_0_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.save_data_hier_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.wifius_gen_music_spectrum_vcvf_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.doa_ants_hier_0, 3))    
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.real_time_scope_hier_0_0_0, 3))    
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.save_data_hier_0, 3))    
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.wifius_gen_music_spectrum_vcvf_0, 3))    
        self.connect((self.doa_ants_hier_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.phase_align_hier_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.phase_align_hier_0, 1), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.phase_align_hier_0, 2), (self.blocks_multiply_const_vxx_0_1, 0))    
        self.connect((self.phase_align_hier_0, 3), (self.blocks_multiply_const_vxx_0_2, 0))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.phase_align_hier_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 1), (self.phase_align_hier_0, 1))    
        self.connect((self.uhd_usrp_source_0_0, 2), (self.phase_align_hier_0, 2))    
        self.connect((self.uhd_usrp_source_0_0, 3), (self.phase_align_hier_0, 3))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.real_time_scope_hier_0_0_0_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 1), (self.real_time_scope_hier_0_0_0_0, 1))    
        self.connect((self.uhd_usrp_source_0_0, 2), (self.real_time_scope_hier_0_0_0_0, 2))    
        self.connect((self.uhd_usrp_source_0_0, 3), (self.real_time_scope_hier_0_0_0_0, 3))    
        self.connect((self.wifius_gen_music_spectrum_vcvf_0, 0), (self.qtgui_vector_sink_f_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "calibration_example_gui")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_antenna_spacing_inches(self):
        return self.antenna_spacing_inches

    def set_antenna_spacing_inches(self, antenna_spacing_inches):
        self.antenna_spacing_inches = antenna_spacing_inches
        self.set_antenna_spacing(self.antenna_spacing_inches*0.0254)

    def get_speed_of_light(self):
        return self.speed_of_light

    def set_speed_of_light(self, speed_of_light):
        self.speed_of_light = speed_of_light
        self.set_center_freq(self.speed_of_light/(2*self.antenna_spacing))

    def get_gain_rx_array(self):
        return self.gain_rx_array

    def set_gain_rx_array(self, gain_rx_array):
        self.gain_rx_array = gain_rx_array
        self.set_gain_rx(self.gain_rx_array)

    def get_antenna_spacing(self):
        return self.antenna_spacing

    def set_antenna_spacing(self, antenna_spacing):
        self.antenna_spacing = antenna_spacing
        self.set_center_freq(self.speed_of_light/(2*self.antenna_spacing))

    def get_window(self):
        return self.window

    def set_window(self, window):
        self.window = window
        self.phase_align_hier_0.set_window(self.window)

    def get_variable_qtgui_chooser_0_1_1(self):
        return self.variable_qtgui_chooser_0_1_1

    def set_variable_qtgui_chooser_0_1_1(self, variable_qtgui_chooser_0_1_1):
        self.variable_qtgui_chooser_0_1_1 = variable_qtgui_chooser_0_1_1
        self._variable_qtgui_chooser_0_1_1_callback(self.variable_qtgui_chooser_0_1_1)
        self.blocks_message_strobe_0_0.set_msg(pmt.from_double(self.variable_qtgui_chooser_0_1_1))

    def get_variable_qtgui_chooser_0_0(self):
        return self.variable_qtgui_chooser_0_0

    def set_variable_qtgui_chooser_0_0(self, variable_qtgui_chooser_0_0):
        self.variable_qtgui_chooser_0_0 = variable_qtgui_chooser_0_0
        self._variable_qtgui_chooser_0_0_callback(self.variable_qtgui_chooser_0_0)
        self.blocks_message_strobe_0.set_msg(pmt.from_double(self.variable_qtgui_chooser_0_0))

    def get_sync(self):
        return self.sync

    def set_sync(self, sync):
        self.sync = sync
        self._sync_callback(self.sync)
        self.blocks_message_strobe_0_1.set_msg(self.sync)

    def get_samples_to_save(self):
        return self.samples_to_save

    def set_samples_to_save(self, samples_to_save):
        self.samples_to_save = samples_to_save

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.real_time_scope_hier_0_0_0.set_samp_rate(self.samp_rate)
        self.real_time_scope_hier_0_0_0_0.set_samp_rate(self.samp_rate)
        self.sync_tx_hier_0.set_samp_rate(self.samp_rate)
        self.target_tx_hier_0.set_samp_rate(self.samp_rate)
        self.target_tx_hier_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_pi(self):
        return self.pi

    def set_pi(self, pi):
        self.pi = pi
        self.blocks_multiply_const_vxx_0.set_k((numpy.exp(-1j*2*self.pi*numpy.sin(self.phase_c0*self.pi/180)), ))
        self.blocks_multiply_const_vxx_0_0.set_k((numpy.exp(-1j*2*self.pi*numpy.sin(self.phase_c1*self.pi/180)), ))
        self.blocks_multiply_const_vxx_0_1.set_k((numpy.exp(-1j*2*self.pi*numpy.sin(self.phase_c2*self.pi/180)), ))
        self.blocks_multiply_const_vxx_0_2.set_k((numpy.exp(-1j*2*self.pi*numpy.sin(self.phase_c3*self.pi/180)), ))

    def get_phase_c3(self):
        return self.phase_c3

    def set_phase_c3(self, phase_c3):
        self.phase_c3 = phase_c3
        self.blocks_multiply_const_vxx_0_2.set_k((numpy.exp(-1j*2*self.pi*numpy.sin(self.phase_c3*self.pi/180)), ))

    def get_phase_c2(self):
        return self.phase_c2

    def set_phase_c2(self, phase_c2):
        self.phase_c2 = phase_c2
        self.blocks_multiply_const_vxx_0_1.set_k((numpy.exp(-1j*2*self.pi*numpy.sin(self.phase_c2*self.pi/180)), ))

    def get_phase_c1(self):
        return self.phase_c1

    def set_phase_c1(self, phase_c1):
        self.phase_c1 = phase_c1
        self.blocks_multiply_const_vxx_0_0.set_k((numpy.exp(-1j*2*self.pi*numpy.sin(self.phase_c1*self.pi/180)), ))

    def get_phase_c0(self):
        return self.phase_c0

    def set_phase_c0(self, phase_c0):
        self.phase_c0 = phase_c0
        self.blocks_multiply_const_vxx_0.set_k((numpy.exp(-1j*2*self.pi*numpy.sin(self.phase_c0*self.pi/180)), ))

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset

    def get_label2(self):
        return self.label2

    def set_label2(self, label2):
        self.label2 = label2
        Qt.QMetaObject.invokeMethod(self._label2_label, "setText", Qt.Q_ARG("QString", str(self.label2)))

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label
        Qt.QMetaObject.invokeMethod(self._label_label, "setText", Qt.Q_ARG("QString", str(self.label)))

    def get_gain_tx2(self):
        return self.gain_tx2

    def set_gain_tx2(self, gain_tx2):
        self.gain_tx2 = gain_tx2
        self.target_tx_hier_0.set_gain_tx2(self.gain_tx2)

    def get_gain_tx1(self):
        return self.gain_tx1

    def set_gain_tx1(self, gain_tx1):
        self.gain_tx1 = gain_tx1
        self.target_tx_hier_0_0.set_gain_tx2(self.gain_tx1)

    def get_gain_rx(self):
        return self.gain_rx

    def set_gain_rx(self, gain_rx):
        self.gain_rx = gain_rx
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 0)
        	
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 1)
        	
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 2)
        	
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 3)
        	

    def get_distant_tx_target(self):
        return self.distant_tx_target

    def set_distant_tx_target(self, distant_tx_target):
        self.distant_tx_target = distant_tx_target
        self._distant_tx_target_callback(self.distant_tx_target)
        self.blocks_message_strobe_0_2_0.set_msg(pmt.from_double(self.distant_tx_target))

    def get_distant_tx(self):
        return self.distant_tx

    def set_distant_tx(self, distant_tx):
        self.distant_tx = distant_tx
        self._distant_tx_callback(self.distant_tx)
        self.blocks_message_strobe_0_2.set_msg(pmt.from_double(self.distant_tx))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.sync_tx_hier_0.set_center_freq(self.center_freq)
        self.target_tx_hier_0.set_center_freq(self.center_freq)
        self.target_tx_hier_0_0.set_center_freq(self.center_freq)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 1)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 2)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 3)

    def get_cal_freq(self):
        return self.cal_freq

    def set_cal_freq(self, cal_freq):
        self.cal_freq = cal_freq

    def get_ant_cal_enable(self):
        return self.ant_cal_enable

    def set_ant_cal_enable(self, ant_cal_enable):
        self.ant_cal_enable = ant_cal_enable
        self._ant_cal_enable_callback(self.ant_cal_enable)
        self.blocks_message_strobe_0_3.set_msg(pmt.from_double(self.ant_cal_enable))


def main(top_block_cls=calibration_example_gui, options=None):

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
