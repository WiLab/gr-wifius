#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Calibration Example
# Author: Travis Collins
# Description: WiFiUS Project
# Generated: Mon Feb  1 16:42:32 2016
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
from doa_hier import doa_hier  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from phase_corrector import phase_corrector  # grc-generated hier_block
from real_time_scope_hier import real_time_scope_hier  # grc-generated hier_block
import ConfigParser
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
        self.speed_of_light = speed_of_light = 299792458
        self.antenna_spacing = antenna_spacing = 0.1
        self.variable_qtgui_chooser_0_0 = variable_qtgui_chooser_0_0 = 0
        self.sync = sync = pmt.PMT_F
        self._samples_to_save_config = ConfigParser.ConfigParser()
        self._samples_to_save_config.read("/home/travis/Dropbox/PHD/WiFiUS/doa/gnuradio/gr-matlab/config.gr")
        try: samples_to_save = self._samples_to_save_config.getfloat("rx", "samples_to_save")
        except: samples_to_save = 2**18
        self.samples_to_save = samples_to_save
        self._samp_rate_config = ConfigParser.ConfigParser()
        self._samp_rate_config.read("/home/travis/Dropbox/PHD/WiFiUS/doa/gnuradio/gr-matlab/config.gr")
        try: samp_rate = self._samp_rate_config.getfloat("system", "sample_rate")
        except: samp_rate = 100000000/64
        self.samp_rate = samp_rate
        self.gain_rx = gain_rx = 0
        self.distant_tx = distant_tx = 1
        self.center_freq = center_freq = speed_of_light/(2*antenna_spacing)
        self._cal_freq_config = ConfigParser.ConfigParser()
        self._cal_freq_config.read("/home/travis/Dropbox/PHD/WiFiUS/doa/gnuradio/gr-matlab/config.gr")
        try: cal_freq = self._cal_freq_config.getfloat("system", "cal_tone_freq")
        except: cal_freq = 1024
        self.cal_freq = cal_freq

        ##################################################
        # Blocks
        ##################################################
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
        self.top_layout.addWidget(self.tab)
        self._sync_options = (pmt.PMT_F, pmt.PMT_T, )
        self._sync_labels = ("Stop", "Running", )
        self._sync_group_box = Qt.QGroupBox("Sync System")
        self._sync_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._sync_button_group = variable_chooser_button_group()
        self._sync_group_box.setLayout(self._sync_box)
        for i, label in enumerate(self._sync_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._sync_box.addWidget(radio_button)
        	self._sync_button_group.addButton(radio_button, i)
        self._sync_callback = lambda i: Qt.QMetaObject.invokeMethod(self._sync_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._sync_options.index(i)))
        self._sync_callback(self.sync)
        self._sync_button_group.buttonClicked[int].connect(
        	lambda i: self.set_sync(self._sync_options[i]))
        self.top_layout.addWidget(self._sync_group_box)
        self._distant_tx_options = (1, 0, )
        self._distant_tx_labels = ("Not Started", "Start Save", )
        self._distant_tx_group_box = Qt.QGroupBox("Distant TX")
        self._distant_tx_box = Qt.QHBoxLayout()
        class variable_chooser_button_group(Qt.QButtonGroup):
            def __init__(self, parent=None):
                Qt.QButtonGroup.__init__(self, parent)
            @pyqtSlot(int)
            def updateButtonChecked(self, button_id):
                self.button(button_id).setChecked(True)
        self._distant_tx_button_group = variable_chooser_button_group()
        self._distant_tx_group_box.setLayout(self._distant_tx_box)
        for i, label in enumerate(self._distant_tx_labels):
        	radio_button = Qt.QRadioButton(label)
        	self._distant_tx_box.addWidget(radio_button)
        	self._distant_tx_button_group.addButton(radio_button, i)
        self._distant_tx_callback = lambda i: Qt.QMetaObject.invokeMethod(self._distant_tx_button_group, "updateButtonChecked", Qt.Q_ARG("int", self._distant_tx_options.index(i)))
        self._distant_tx_callback(self.distant_tx)
        self._distant_tx_button_group.buttonClicked[int].connect(
        	lambda i: self.set_distant_tx(self._distant_tx_options[i]))
        self.top_layout.addWidget(self._distant_tx_group_box)
        self.wifius_blocker_0_0 = wifius.blocker(True)
        self.wifius_blocker_0 = wifius.blocker(False)
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
        self.uhd_usrp_sink_0_0_0_0 = uhd.usrp_sink(
        	",".join(("addr=192.168.80.2", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0_0_0_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)
        self.uhd_usrp_sink_0_0_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0_0_0_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_sink_0_0_0_0.set_gain(30, 0)
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
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	64, #size
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
        self.phase_corrector_0_0_0 = phase_corrector(
            window=1024,
        )
        self.phase_corrector_0_0 = phase_corrector(
            window=1024,
        )
        self.phase_corrector_0 = phase_corrector(
            window=1024,
        )
        self.doa_hier_0 = doa_hier()
        self.blocks_message_strobe_0_2 = blocks.message_strobe(pmt.from_double(distant_tx), 1000)
        self.blocks_message_strobe_0_1 = blocks.message_strobe(sync, 1000)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.from_double(variable_qtgui_chooser_0_0), 1000)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, cal_freq, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, cal_freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.wifius_blocker_0, 'enable_stop'))    
        self.msg_connect((self.blocks_message_strobe_0_1, 'strobe'), (self.phase_corrector_0, 'in'))    
        self.msg_connect((self.blocks_message_strobe_0_1, 'strobe'), (self.phase_corrector_0_0, 'in'))    
        self.msg_connect((self.blocks_message_strobe_0_1, 'strobe'), (self.phase_corrector_0_0_0, 'in'))    
        self.msg_connect((self.blocks_message_strobe_0_2, 'strobe'), (self.wifius_blocker_0_0, 'enable_stop'))    
        self.connect((self.analog_sig_source_x_0, 0), (self.wifius_blocker_0, 0))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.wifius_blocker_0_0, 0))    
        self.connect((self.doa_hier_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.phase_corrector_0, 0), (self.doa_hier_0, 1))    
        self.connect((self.phase_corrector_0, 0), (self.real_time_scope_hier_0_0_0, 1))    
        self.connect((self.phase_corrector_0_0, 0), (self.doa_hier_0, 2))    
        self.connect((self.phase_corrector_0_0, 0), (self.real_time_scope_hier_0_0_0, 2))    
        self.connect((self.phase_corrector_0_0_0, 0), (self.doa_hier_0, 3))    
        self.connect((self.phase_corrector_0_0_0, 0), (self.real_time_scope_hier_0_0_0, 3))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.doa_hier_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.phase_corrector_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 1), (self.phase_corrector_0, 1))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.phase_corrector_0_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 2), (self.phase_corrector_0_0, 1))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.phase_corrector_0_0_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 3), (self.phase_corrector_0_0_0, 1))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.real_time_scope_hier_0_0_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 0), (self.real_time_scope_hier_0_0_0_0, 0))    
        self.connect((self.uhd_usrp_source_0_0, 1), (self.real_time_scope_hier_0_0_0_0, 1))    
        self.connect((self.uhd_usrp_source_0_0, 2), (self.real_time_scope_hier_0_0_0_0, 2))    
        self.connect((self.uhd_usrp_source_0_0, 3), (self.real_time_scope_hier_0_0_0_0, 3))    
        self.connect((self.wifius_blocker_0, 0), (self.uhd_usrp_sink_0_0, 0))    
        self.connect((self.wifius_blocker_0_0, 0), (self.uhd_usrp_sink_0_0_0_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "calibration_example_gui")
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
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.real_time_scope_hier_0_0_0.set_samp_rate(self.samp_rate)
        self.real_time_scope_hier_0_0_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0_0_0_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)

    def get_gain_rx(self):
        return self.gain_rx

    def set_gain_rx(self, gain_rx):
        self.gain_rx = gain_rx
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 0)
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 1)
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 2)
        self.uhd_usrp_source_0_0.set_gain(self.gain_rx, 3)

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
        self.uhd_usrp_sink_0_0.set_center_freq(self.center_freq, 0)
        self.uhd_usrp_sink_0_0_0_0.set_center_freq(self.center_freq, 0)
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


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = calibration_example_gui()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
