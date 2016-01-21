#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block Usrp New Diff Test
# Generated: Thu Jan 21 11:20:37 2016
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
from correct_gains_hier import correct_gains_hier  # grc-generated hier_block
from delay_correct_hier import delay_correct_hier  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt
import sip
import time


class top_block_usrp_new_diff_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block Usrp New Diff Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block Usrp New Diff Test")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block_usrp_new_diff_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_chooser_0_1_0 = variable_qtgui_chooser_0_1_0 = 0
        self.variable_qtgui_chooser_0_0 = variable_qtgui_chooser_0_0 = 0
        self.samp_rate = samp_rate = 100000000/256
        self.gain_rx = gain_rx = 0
        self.enabler = enabler = 0
        self.center_freq = center_freq = 2.4e9
        self.cal_tone_freq = cal_tone_freq = 1000
        self.cal_freq = cal_freq = 1000

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
        self.uhd_usrp_source_0_0.set_time_unknown_pps(uhd.time_spec())
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0_0.set_gain(gain_rx, 0)
        self.uhd_usrp_source_0_0.set_center_freq(center_freq, 1)
        self.uhd_usrp_source_0_0.set_gain(gain_rx, 1)
        self.uhd_usrp_source_0_0.set_center_freq(center_freq, 2)
        self.uhd_usrp_source_0_0.set_gain(gain_rx, 2)
        self.uhd_usrp_sink_0_0_0 = uhd.usrp_sink(
        	",".join(("addr=192.168.40.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0_0_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_sink_0_0_0.set_gain(10, 0)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
        	100, #size
        	samp_rate, #samp_rate
        	"Input", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()
        
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
        
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.tab_layout_0.addWidget(self._qtgui_time_sink_x_0_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	100, #size
        	samp_rate, #samp_rate
        	"Post Gain Correct", #name
        	2 #number of inputs
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
        
        for i in xrange(2):
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
        self.tab_layout_1.addWidget(self._qtgui_time_sink_x_0_win)
        self._enabler_options = (0, 1, )
        self._enabler_labels = ("Enable", "Disable", )
        self._enabler_group_box = Qt.QGroupBox("Gain Correct (Do Not Renable)")
        self._enabler_box = Qt.QVBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._enabler_button_group = variable_chooser_button_group()
        self._enabler_group_box.setLayout(self._enabler_box)
        for i, label in enumerate(self._enabler_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._enabler_box.addWidget(radio_button)
        	self._enabler_button_group.addButton(radio_button, i)
        self._enabler_callback = lambda i: Qt.QMetaObject.invokeMethod(self._enabler_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._enabler_options.index(i)))
        self._enabler_callback(self.enabler)
        self._enabler_button_group.buttonClicked[int].connect(
        	lambda i: self.set_enabler(self._enabler_options[i]))
        self.top_layout.addWidget(self._enabler_group_box)
        self.delay_correct_hier_0 = delay_correct_hier(
            cal_tone_freq=cal_freq,
            samp_rate=samp_rate,
        )
        self.correct_gains_hier_0 = correct_gains_hier(
            cal_tone_freq=cal_freq,
            samp_rate_0=samp_rate,
        )
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.from_double(variable_qtgui_chooser_0_1_0), 1000)
        self.blocks_complex_to_real_0_2 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0_0_2 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, cal_freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.correct_gains_hier_0, 'Trigger'))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.uhd_usrp_sink_0_0_0, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.blocks_complex_to_real_0_0_2, 0), (self.qtgui_time_sink_x_0_1, 1))    
        self.connect((self.blocks_complex_to_real_0_2, 0), (self.qtgui_time_sink_x_0_1, 0))    
        self.connect((self.correct_gains_hier_0, 2), (self.blocks_null_sink_0, 0))    
        self.connect((self.correct_gains_hier_0, 0), (self.delay_correct_hier_0, 0))    
        self.connect((self.correct_gains_hier_0, 1), (self.delay_correct_hier_0, 1))    
        self.connect((self.delay_correct_hier_0, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.delay_correct_hier_0, 1), (self.blocks_complex_to_real_0_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 1), (self.blocks_complex_to_real_0_0_2, 0))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.blocks_complex_to_real_0_2, 0))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.correct_gains_hier_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 1), (self.correct_gains_hier_0, 1))    
        self.connect((self.uhd_usrp_source_0_0, 2), (self.correct_gains_hier_0, 2))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block_usrp_new_diff_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

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
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.correct_gains_hier_0.set_samp_rate_0(self.samp_rate)
        self.delay_correct_hier_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)

    def get_gain_rx(self):
        return self.gain_rx

    def set_gain_rx(self, gain_rx):
        self.gain_rx = gain_rx
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 0)
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 1)
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 2)

    def get_enabler(self):
        return self.enabler

    def set_enabler(self, enabler):
        self.enabler = enabler
        self._enabler_callback(self.enabler)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.uhd_usrp_sink_0_0_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 1)
        self.uhd_usrp_source_0_0.set_center_freq(self.center_freq, 2)

    def get_cal_tone_freq(self):
        return self.cal_tone_freq

    def set_cal_tone_freq(self, cal_tone_freq):
        self.cal_tone_freq = cal_tone_freq

    def get_cal_freq(self):
        return self.cal_freq

    def set_cal_freq(self, cal_freq):
        self.cal_freq = cal_freq
        self.analog_sig_source_x_0_0.set_frequency(self.cal_freq)
        self.correct_gains_hier_0.set_cal_tone_freq(self.cal_freq)
        self.delay_correct_hier_0.set_cal_tone_freq(self.cal_freq)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_block_usrp_new_diff_test()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
