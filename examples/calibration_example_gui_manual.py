#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Calibration Example
# Author: Travis Collins
# Description: WiFiUS Project
# Generated: Sun Jan 31 21:10:28 2016
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
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
from real_time_scope_hier import real_time_scope_hier  # grc-generated hier_block
from save_data_hier import save_data_hier  # grc-generated hier_block
import numpy
import pmt
import time


class calibration_example_gui_manual(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "calibration_example_gui_manual")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.speed_of_light = speed_of_light = 299792458
        self.antenna_spacing = antenna_spacing = 0.1
        self.variable_qtgui_chooser_0_1_1 = variable_qtgui_chooser_0_1_1 = 1
        self.variable_qtgui_chooser_0_1_0 = variable_qtgui_chooser_0_1_0 = 0
        self.variable_qtgui_chooser_0_0_0 = variable_qtgui_chooser_0_0_0 = 1
        self.variable_qtgui_chooser_0_0 = variable_qtgui_chooser_0_0 = 0
        self.samp_rate = samp_rate = 100000000/64
        self.gain_rx = gain_rx = 0
        self.center_freq = center_freq = speed_of_light/(2*antenna_spacing)
        self.cal_freq = cal_freq = 1024
        self.Shift_1 = Shift_1 = -4
        self.Shift_0 = Shift_0 = -4
        self.Shift = Shift = -4

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_chooser_0_1_1_options = (1, 0, )
        self._variable_qtgui_chooser_0_1_1_labels = ("Not Started", "Start Save", )
        self._variable_qtgui_chooser_0_1_1_group_box = Qt.QGroupBox("Trigger Data Save")
        self._variable_qtgui_chooser_0_1_1_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._variable_qtgui_chooser_0_1_1_button_group = variable_chooser_button_group()
        self._variable_qtgui_chooser_0_1_1_group_box.setLayout(self._variable_qtgui_chooser_0_1_1_box)
        for i, label in enumerate(self._variable_qtgui_chooser_0_1_1_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._variable_qtgui_chooser_0_1_1_box.addWidget(radio_button)
        	self._variable_qtgui_chooser_0_1_1_button_group.addButton(radio_button, i)
        self._variable_qtgui_chooser_0_1_1_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_0_1_1_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._variable_qtgui_chooser_0_1_1_options.index(i)))
        self._variable_qtgui_chooser_0_1_1_callback(self.variable_qtgui_chooser_0_1_1)
        self._variable_qtgui_chooser_0_1_1_button_group.buttonClicked[int].connect(
        	lambda i: self.set_variable_qtgui_chooser_0_1_1(self._variable_qtgui_chooser_0_1_1_options[i]))
        self.top_layout.addWidget(self._variable_qtgui_chooser_0_1_1_group_box)
        self._variable_qtgui_chooser_0_0_0_options = (0, 1, )
        self._variable_qtgui_chooser_0_0_0_labels = ("Enable", "Disable", )
        self._variable_qtgui_chooser_0_0_0_group_box = Qt.QGroupBox("Distant Transmitter Enable")
        self._variable_qtgui_chooser_0_0_0_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._variable_qtgui_chooser_0_0_0_button_group = variable_chooser_button_group()
        self._variable_qtgui_chooser_0_0_0_group_box.setLayout(self._variable_qtgui_chooser_0_0_0_box)
        for i, label in enumerate(self._variable_qtgui_chooser_0_0_0_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._variable_qtgui_chooser_0_0_0_box.addWidget(radio_button)
        	self._variable_qtgui_chooser_0_0_0_button_group.addButton(radio_button, i)
        self._variable_qtgui_chooser_0_0_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_0_0_0_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._variable_qtgui_chooser_0_0_0_options.index(i)))
        self._variable_qtgui_chooser_0_0_0_callback(self.variable_qtgui_chooser_0_0_0)
        self._variable_qtgui_chooser_0_0_0_button_group.buttonClicked[int].connect(
        	lambda i: self.set_variable_qtgui_chooser_0_0_0(self._variable_qtgui_chooser_0_0_0_options[i]))
        self.top_layout.addWidget(self._variable_qtgui_chooser_0_0_0_group_box)
        self._variable_qtgui_chooser_0_0_options = (0, 1, )
        self._variable_qtgui_chooser_0_0_labels = ("Enable", "Disable", )
        self._variable_qtgui_chooser_0_0_group_box = Qt.QGroupBox("Source Enable")
        self._variable_qtgui_chooser_0_0_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._variable_qtgui_chooser_0_0_button_group = variable_chooser_button_group()
        self._variable_qtgui_chooser_0_0_group_box.setLayout(self._variable_qtgui_chooser_0_0_box)
        for i, label in enumerate(self._variable_qtgui_chooser_0_0_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._variable_qtgui_chooser_0_0_box.addWidget(radio_button)
        	self._variable_qtgui_chooser_0_0_button_group.addButton(radio_button, i)
        self._variable_qtgui_chooser_0_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_0_0_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._variable_qtgui_chooser_0_0_options.index(i)))
        self._variable_qtgui_chooser_0_0_callback(self.variable_qtgui_chooser_0_0)
        self._variable_qtgui_chooser_0_0_button_group.buttonClicked[int].connect(
        	lambda i: self.set_variable_qtgui_chooser_0_0(self._variable_qtgui_chooser_0_0_options[i]))
        self.top_layout.addWidget(self._variable_qtgui_chooser_0_0_group_box)
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
        self.tab.addTab(self.tab_widget_1, "Post Gain Correct")
        self.tab_widget_2 = Qt.QWidget()
        self.tab_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_widget_2)
        self.tab_grid_layout_2 = Qt.QGridLayout()
        self.tab_layout_2.addLayout(self.tab_grid_layout_2)
        self.tab.addTab(self.tab_widget_2, "Post Phase Correct")
        self.top_layout.addWidget(self.tab)
        self._Shift_1_range = Range(-4, 4, 0.01, -4, 200)
        self._Shift_1_win = RangeWidget(self._Shift_1_range, self.set_Shift_1, "Shift", "counter_slider", float)
        self.top_layout.addWidget(self._Shift_1_win)
        self._Shift_0_range = Range(-4, 4, 0.01, -4, 200)
        self._Shift_0_win = RangeWidget(self._Shift_0_range, self.set_Shift_0, "Shift", "counter_slider", float)
        self.top_layout.addWidget(self._Shift_0_win)
        self._Shift_range = Range(-4, 4, 0.01, -4, 200)
        self._Shift_win = RangeWidget(self._Shift_range, self.set_Shift, "Shift", "counter_slider", float)
        self.top_layout.addWidget(self._Shift_win)
        self._variable_qtgui_chooser_0_1_0_options = (1, 0, )
        self._variable_qtgui_chooser_0_1_0_labels = ("Stop", "Running", )
        self._variable_qtgui_chooser_0_1_0_group_box = Qt.QGroupBox("Sync System")
        self._variable_qtgui_chooser_0_1_0_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._variable_qtgui_chooser_0_1_0_button_group = variable_chooser_button_group()
        self._variable_qtgui_chooser_0_1_0_group_box.setLayout(self._variable_qtgui_chooser_0_1_0_box)
        for i, label in enumerate(self._variable_qtgui_chooser_0_1_0_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._variable_qtgui_chooser_0_1_0_box.addWidget(radio_button)
        	self._variable_qtgui_chooser_0_1_0_button_group.addButton(radio_button, i)
        self._variable_qtgui_chooser_0_1_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_0_1_0_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._variable_qtgui_chooser_0_1_0_options.index(i)))
        self._variable_qtgui_chooser_0_1_0_callback(self.variable_qtgui_chooser_0_1_0)
        self._variable_qtgui_chooser_0_1_0_button_group.buttonClicked[int].connect(
        	lambda i: self.set_variable_qtgui_chooser_0_1_0(self._variable_qtgui_chooser_0_1_0_options[i]))
        self.top_layout.addWidget(self._variable_qtgui_chooser_0_1_0_group_box)
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
        	",".join(("addr0=192.168.70.2,addr1=192.168.20.2,addr2=192.168.30.2,addr3=192.168.50.2", "")),
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
        self.uhd_usrp_source_0_0.set_center_freq(center_freq, 1)
        self.uhd_usrp_source_0_0.set_gain(gain_rx, 1)
        self.uhd_usrp_source_0_0.set_center_freq(center_freq, 2)
        self.uhd_usrp_source_0_0.set_gain(gain_rx, 2)
        self.uhd_usrp_source_0_0.set_center_freq(center_freq, 3)
        self.uhd_usrp_source_0_0.set_gain(gain_rx, 3)
        self.uhd_usrp_sink_0_0_0 = uhd.usrp_sink(
        	",".join(("addr=192.168.80.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0_0_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_sink_0_0_0.set_gain(30, 0)
        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
        	",".join(("addr=192.168.40.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0_0.set_clock_source("mimo", 0)
        self.uhd_usrp_sink_0_0.set_time_source("mimo", 0)
        self.uhd_usrp_sink_0_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_sink_0_0.set_gain(10, 0)
        self.save_data_hier_0 = save_data_hier(
            keep=1,
            samples=2**22,
            skips=2**18,
            vec_size=1,
        )
        self.real_time_scope_hier_0_0_0 = real_time_scope_hier(
            npoints=3000,
            samp_rate=samp_rate,
        )
        self.tab_layout_2.addWidget(self.real_time_scope_hier_0_0_0)
        self.real_time_scope_hier_0 = real_time_scope_hier(
            npoints=3000,
            samp_rate=samp_rate,
        )
        self.tab_layout_0.addWidget(self.real_time_scope_hier_0)
        self.blocks_multiply_const_vxx_0_2 = blocks.multiply_const_vcc((complex(numpy.cos(Shift_1),numpy.sin(Shift_1)), ))
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_vcc((complex(numpy.cos(Shift_0),numpy.sin(Shift_0)), ))
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_vcc((complex(numpy.cos(Shift),numpy.sin(Shift)), ))
        self.blocks_message_strobe_0_0 = blocks.message_strobe(pmt.from_double(variable_qtgui_chooser_0_1_1), 1000)
        self.blks2_valve_0_0 = grc_blks2.valve(item_size=gr.sizeof_gr_complex*1, open=bool(variable_qtgui_chooser_0_0_0))
        self.blks2_valve_0 = grc_blks2.valve(item_size=gr.sizeof_gr_complex*1, open=bool(variable_qtgui_chooser_0_0))
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, cal_freq, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, cal_freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0_0, 'strobe'), (self.save_data_hier_0, 'Trigger'))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blks2_valve_0, 0))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blks2_valve_0_0, 0))    
        self.connect((self.blks2_valve_0, 0), (self.uhd_usrp_sink_0_0, 0))    
        self.connect((self.blks2_valve_0_0, 0), (self.uhd_usrp_sink_0_0_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.real_time_scope_hier_0_0_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.save_data_hier_0, 1))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.real_time_scope_hier_0_0_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.save_data_hier_0, 2))    
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.real_time_scope_hier_0_0_0, 3))    
        self.connect((self.blocks_multiply_const_vxx_0_2, 0), (self.save_data_hier_0, 3))    
        self.connect((self.uhd_usrp_source_0_0, 1), (self.blocks_multiply_const_vxx_0_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 2), (self.blocks_multiply_const_vxx_0_1, 0))    
        self.connect((self.uhd_usrp_source_0_0, 3), (self.blocks_multiply_const_vxx_0_2, 0))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.real_time_scope_hier_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 1), (self.real_time_scope_hier_0, 1))    
        self.connect((self.uhd_usrp_source_0_0, 2), (self.real_time_scope_hier_0, 2))    
        self.connect((self.uhd_usrp_source_0_0, 3), (self.real_time_scope_hier_0, 3))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.real_time_scope_hier_0_0_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.save_data_hier_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "calibration_example_gui_manual")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_speed_of_light(self):
        return self.speed_of_light

    def set_speed_of_light(self, speed_of_light):
        self.speed_of_light = speed_of_light
        self.set_center_freq(self.speed_of_light/(2*self.antenna_spacing))

    def get_antenna_spacing(self):
        return self.antenna_spacing

    def set_antenna_spacing(self, antenna_spacing):
        self.antenna_spacing = antenna_spacing
        self.set_center_freq(self.speed_of_light/(2*self.antenna_spacing))

    def get_variable_qtgui_chooser_0_1_1(self):
        return self.variable_qtgui_chooser_0_1_1

    def set_variable_qtgui_chooser_0_1_1(self, variable_qtgui_chooser_0_1_1):
        self.variable_qtgui_chooser_0_1_1 = variable_qtgui_chooser_0_1_1
        self._variable_qtgui_chooser_0_1_1_callback(self.variable_qtgui_chooser_0_1_1)
        self.blocks_message_strobe_0_0.set_msg(pmt.from_double(self.variable_qtgui_chooser_0_1_1))

    def get_variable_qtgui_chooser_0_1_0(self):
        return self.variable_qtgui_chooser_0_1_0

    def set_variable_qtgui_chooser_0_1_0(self, variable_qtgui_chooser_0_1_0):
        self.variable_qtgui_chooser_0_1_0 = variable_qtgui_chooser_0_1_0
        self._variable_qtgui_chooser_0_1_0_callback(self.variable_qtgui_chooser_0_1_0)

    def get_variable_qtgui_chooser_0_0_0(self):
        return self.variable_qtgui_chooser_0_0_0

    def set_variable_qtgui_chooser_0_0_0(self, variable_qtgui_chooser_0_0_0):
        self.variable_qtgui_chooser_0_0_0 = variable_qtgui_chooser_0_0_0
        self._variable_qtgui_chooser_0_0_0_callback(self.variable_qtgui_chooser_0_0_0)
        self.blks2_valve_0_0.set_open(bool(self.variable_qtgui_chooser_0_0_0))

    def get_variable_qtgui_chooser_0_0(self):
        return self.variable_qtgui_chooser_0_0

    def set_variable_qtgui_chooser_0_0(self, variable_qtgui_chooser_0_0):
        self.variable_qtgui_chooser_0_0 = variable_qtgui_chooser_0_0
        self._variable_qtgui_chooser_0_0_callback(self.variable_qtgui_chooser_0_0)
        self.blks2_valve_0.set_open(bool(self.variable_qtgui_chooser_0_0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.real_time_scope_hier_0.set_samp_rate(self.samp_rate)
        self.real_time_scope_hier_0_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)

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
        self.uhd_usrp_sink_0_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_sink_0_0_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 1)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 2)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 3)

    def get_cal_freq(self):
        return self.cal_freq

    def set_cal_freq(self, cal_freq):
        self.cal_freq = cal_freq
        self.analog_sig_source_x_0.set_frequency(self.cal_freq)
        self.analog_sig_source_x_0_0.set_frequency(self.cal_freq)

    def get_Shift_1(self):
        return self.Shift_1

    def set_Shift_1(self, Shift_1):
        self.Shift_1 = Shift_1
        self.blocks_multiply_const_vxx_0_2.set_k((complex(numpy.cos(self.Shift_1),numpy.sin(self.Shift_1)), ))

    def get_Shift_0(self):
        return self.Shift_0

    def set_Shift_0(self, Shift_0):
        self.Shift_0 = Shift_0
        self.blocks_multiply_const_vxx_0_1.set_k((complex(numpy.cos(self.Shift_0),numpy.sin(self.Shift_0)), ))

    def get_Shift(self):
        return self.Shift

    def set_Shift(self, Shift):
        self.Shift = Shift
        self.blocks_multiply_const_vxx_0_0.set_k((complex(numpy.cos(self.Shift),numpy.sin(self.Shift)), ))


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = calibration_example_gui_manual()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
