#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Calibration Example
# Author: Travis Collins
# Description: WiFiUS Project
# Generated: Sun Jan 31 16:38:47 2016
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
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from measure_offset import measure_offset  # grc-generated hier_block
from optparse import OptionParser
import pmt
import sip
import time


class calibration_example_gui_2x_measure(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "calibration_example_gui_2x_measure")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.speed_of_light = speed_of_light = 299792458
        self.antenna_spacing = antenna_spacing = 0.1
        self.variable_qtgui_chooser_0_1_0 = variable_qtgui_chooser_0_1_0 = 0
        self.variable_qtgui_chooser_0_0 = variable_qtgui_chooser_0_0 = 1
        self.samp_rate = samp_rate = 100000000/64
        self.gain_rx = gain_rx = 0
        self.center_freq = center_freq = speed_of_light/(2*antenna_spacing)
        self.cal_freq = cal_freq = 1024

        ##################################################
        # Blocks
        ##################################################
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
        self._variable_qtgui_chooser_0_0_options = (0, 1, )
        self._variable_qtgui_chooser_0_0_labels = ("Enable", "Disable", )
        self._variable_qtgui_chooser_0_0_group_box = Qt.QGroupBox("Source Enable")
        self._variable_qtgui_chooser_0_0_box = Qt.QVBoxLayout()
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
        self.uhd_usrp_source_0_0_0 = uhd.usrp_source(
        	",".join(("addr0=192.168.70.2,addr1=192.168.20.2,addr2=192.168.30.2,addr3=192.168.50.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(4),
        	),
        )
        self.uhd_usrp_source_0_0_0.set_clock_source("external", 0)
        self.uhd_usrp_source_0_0_0.set_time_source("external", 0)
        self.uhd_usrp_source_0_0_0.set_clock_source("external", 1)
        self.uhd_usrp_source_0_0_0.set_time_source("external", 1)
        self.uhd_usrp_source_0_0_0.set_clock_source("external", 2)
        self.uhd_usrp_source_0_0_0.set_time_source("external", 2)
        self.uhd_usrp_source_0_0_0.set_clock_source("external", 3)
        self.uhd_usrp_source_0_0_0.set_time_source("external", 3)
        self.uhd_usrp_source_0_0_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_source_0_0_0.set_samp_rate(samp_rate)

        # Tell boards to run these commands at this specific time in the future
        cmd_time = self.uhd_usrp_source_0_0_0.get_time_now() + uhd.time_spec_t(1.0)
        self.uhd_usrp_source_0_0_0.set_command_time(cmd_time,0)
        self.uhd_usrp_source_0_0_0.set_command_time(cmd_time,1)
        self.uhd_usrp_source_0_0_0.set_command_time(cmd_time,2)
        self.uhd_usrp_source_0_0_0.set_command_time(cmd_time,3)

        self.uhd_usrp_source_0_0_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0_0_0.set_gain(gain_rx, 0)
        self.uhd_usrp_source_0_0_0.set_center_freq(center_freq, 1)
        self.uhd_usrp_source_0_0_0.set_gain(gain_rx, 1)
        self.uhd_usrp_source_0_0_0.set_center_freq(center_freq, 2)
        self.uhd_usrp_source_0_0_0.set_gain(gain_rx, 2)
        self.uhd_usrp_source_0_0_0.set_center_freq(center_freq, 3)
        self.uhd_usrp_source_0_0_0.set_gain(gain_rx, 3)

        self.uhd_usrp_source_0_0_0.clear_command_time()
        time.sleep(1.5)

        self.uhd_usrp_sink_0_0 = uhd.usrp_sink(
        	",".join(("addr=192.168.40.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0_0.set_clock_source("mimo", 0)
        self.uhd_usrp_sink_0_0.set_time_source("mimo", 0)
        self.uhd_usrp_sink_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_sink_0_0.set_gain(10, 0)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	100, #size
        	samp_rate, #samp_rate
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label("Amplitude", "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_control_panel(True)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ["", "", "", "", "",
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
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1526*2, #size
        	samp_rate, #samp_rate
        	"", #name
        	4 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
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
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(4):
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
        self.measure_offset_0 = measure_offset(
            cal_freq=cal_freq,
            mu=0.0001,
            samp_rate=samp_rate,
        )
        self.blocks_skiphead_0_1 = blocks.skiphead(gr.sizeof_int*1, 1024*4)
        self.blocks_skiphead_0_0 = blocks.skiphead(gr.sizeof_int*1, 1024*4)
        self.blocks_skiphead_0 = blocks.skiphead(gr.sizeof_int*1, 1024*4)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.from_double(variable_qtgui_chooser_0_1_0), 1000)
        self.blocks_int_to_float_0_1 = blocks.int_to_float(1, 1)
        self.blocks_int_to_float_0_0 = blocks.int_to_float(1, 1)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.blocks_head_0 = blocks.head(gr.sizeof_int*1, 100)
        self.blocks_file_sink_0_1 = blocks.file_sink(gr.sizeof_int*1, "/home/travis/Dropbox/PHD/WiFiUS/doa/gnuradio/gr-wifius/data/offsets_chan3_ints.bin", False)
        self.blocks_file_sink_0_1.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_int*1, "/home/travis/Dropbox/PHD/WiFiUS/doa/gnuradio/gr-wifius/data/offsets_chan2_ints.bin", False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_int*1, "/home/travis/Dropbox/PHD/WiFiUS/doa/gnuradio/gr-wifius/data/offsets_chan1_ints.bin", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_real_1_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_1 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, cal_freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.measure_offset_0, 'in'))
        self.connect((self.analog_sig_source_x_0, 0), (self.uhd_usrp_sink_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_complex_to_real_1, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_complex_to_real_1_0, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.blocks_head_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_int_to_float_0_0, 0), (self.qtgui_time_sink_x_0_0, 2))
        self.connect((self.blocks_int_to_float_0_1, 0), (self.qtgui_time_sink_x_0_0, 1))
        self.connect((self.blocks_skiphead_0, 0), (self.blocks_head_0, 0))
        self.connect((self.blocks_skiphead_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_skiphead_0_1, 0), (self.blocks_file_sink_0_1, 0))
        self.connect((self.measure_offset_0, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.measure_offset_0, 2), (self.blocks_int_to_float_0_0, 0))
        self.connect((self.measure_offset_0, 1), (self.blocks_int_to_float_0_1, 0))
        self.connect((self.measure_offset_0, 0), (self.blocks_skiphead_0, 0))
        self.connect((self.measure_offset_0, 1), (self.blocks_skiphead_0_0, 0))
        self.connect((self.measure_offset_0, 2), (self.blocks_skiphead_0_1, 0))
        self.connect((self.uhd_usrp_source_0_0_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.uhd_usrp_source_0_0_0, 2), (self.blocks_complex_to_real_0_0, 0))
        self.connect((self.uhd_usrp_source_0_0_0, 1), (self.blocks_complex_to_real_1, 0))
        self.connect((self.uhd_usrp_source_0_0_0, 3), (self.blocks_complex_to_real_1_0, 0))
        self.connect((self.uhd_usrp_source_0_0_0, 0), (self.measure_offset_0, 0))
        self.connect((self.uhd_usrp_source_0_0_0, 1), (self.measure_offset_0, 1))
        self.connect((self.uhd_usrp_source_0_0_0, 2), (self.measure_offset_0, 2))
        self.connect((self.uhd_usrp_source_0_0_0, 3), (self.measure_offset_0, 3))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "calibration_example_gui_2x_measure")
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

    def get_variable_qtgui_chooser_0_1_0(self):
        return self.variable_qtgui_chooser_0_1_0

    def set_variable_qtgui_chooser_0_1_0(self, variable_qtgui_chooser_0_1_0):
        self.variable_qtgui_chooser_0_1_0 = variable_qtgui_chooser_0_1_0
        self._variable_qtgui_chooser_0_1_0_callback(self.variable_qtgui_chooser_0_1_0)
        self.blocks_message_strobe_0.set_msg(pmt.from_double(self.variable_qtgui_chooser_0_1_0))

    def get_variable_qtgui_chooser_0_0(self):
        return self.variable_qtgui_chooser_0_0

    def set_variable_qtgui_chooser_0_0(self, variable_qtgui_chooser_0_0):
        self.variable_qtgui_chooser_0_0 = variable_qtgui_chooser_0_0
        self._variable_qtgui_chooser_0_0_callback(self.variable_qtgui_chooser_0_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.measure_offset_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0_0_0.set_samp_rate(self.samp_rate)

    def get_gain_rx(self):
        return self.gain_rx

    def set_gain_rx(self, gain_rx):
        self.gain_rx = gain_rx
        self.uhd_usrp_source_0_0_0.set_gain(self.gain_rx, 0)
        self.uhd_usrp_source_0_0_0.set_gain(self.gain_rx, 1)
        self.uhd_usrp_source_0_0_0.set_gain(self.gain_rx, 2)
        self.uhd_usrp_source_0_0_0.set_gain(self.gain_rx, 3)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.uhd_usrp_sink_0_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_source_0_0_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_source_0_0_0.set_center_freq(self.center_freq, 1)
        self.uhd_usrp_source_0_0_0.set_center_freq(self.center_freq, 2)
        self.uhd_usrp_source_0_0_0.set_center_freq(self.center_freq, 3)

    def get_cal_freq(self):
        return self.cal_freq

    def set_cal_freq(self, cal_freq):
        self.cal_freq = cal_freq
        self.analog_sig_source_x_0.set_frequency(self.cal_freq)
        self.measure_offset_0.set_cal_freq(self.cal_freq)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = calibration_example_gui_2x_measure()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
