#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Test Shift And Measure
# Generated: Mon Jan 25 08:49:59 2016
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
from delay_correct_hier import delay_correct_hier  # grc-generated hier_block
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import pmt
import sip


class test_shift_and_measure(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Test Shift And Measure")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Test Shift And Measure")
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

        self.settings = Qt.QSettings("GNU Radio", "test_shift_and_measure")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 100000000/256
        self.cal_tone_freq = cal_tone_freq = 1024
        self.vec_size = vec_size = int(2**( numpy.ceil(numpy.log(samp_rate/cal_tone_freq)/numpy.log(2))))
        self.variable_qtgui_range_0_0 = variable_qtgui_range_0_0 = 0
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 0
        self.variable_qtgui_chooser_0_1_0 = variable_qtgui_chooser_0_1_0 = 0

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_0_0_range = Range(-100, 100, 1, 0, 200)
        self._variable_qtgui_range_0_0_win = RangeWidget(self._variable_qtgui_range_0_0_range, self.set_variable_qtgui_range_0_0, "variable_qtgui_range_0_0", "counter_slider", int)
        self.top_layout.addWidget(self._variable_qtgui_range_0_0_win)
        self._variable_qtgui_range_0_range = Range(-100, 100, 1, 0, 200)
        self._variable_qtgui_range_0_win = RangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, "variable_qtgui_range_0", "counter_slider", int)
        self.top_layout.addWidget(self._variable_qtgui_range_0_win)
        self._variable_qtgui_chooser_0_1_0_options = (1, 0, )
        self._variable_qtgui_chooser_0_1_0_labels = ("Stop", "Running", )
        self._variable_qtgui_chooser_0_1_0_tool_bar = Qt.QToolBar(self)
        self._variable_qtgui_chooser_0_1_0_tool_bar.addWidget(Qt.QLabel("Sync System"+": "))
        self._variable_qtgui_chooser_0_1_0_combo_box = Qt.QComboBox()
        self._variable_qtgui_chooser_0_1_0_tool_bar.addWidget(self._variable_qtgui_chooser_0_1_0_combo_box)
        for label in self._variable_qtgui_chooser_0_1_0_labels: self._variable_qtgui_chooser_0_1_0_combo_box.addItem(label)
        self._variable_qtgui_chooser_0_1_0_callback = lambda i: Qt.QMetaObject.invokeMethod(self._variable_qtgui_chooser_0_1_0_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._variable_qtgui_chooser_0_1_0_options.index(i)))
        self._variable_qtgui_chooser_0_1_0_callback(self.variable_qtgui_chooser_0_1_0)
        self._variable_qtgui_chooser_0_1_0_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_variable_qtgui_chooser_0_1_0(self._variable_qtgui_chooser_0_1_0_options[i]))
        self.top_layout.addWidget(self._variable_qtgui_chooser_0_1_0_tool_bar)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1000, #size
        	1, #samp_rate
        	"", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-0.003, 0.003)
        
        self.qtgui_time_sink_x_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_AUTO, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        
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
        self.delay_correct_hier_0_0_0 = delay_correct_hier(
            cal_tone_freq=cal_tone_freq,
            mu=0.001,
            samp_rate=samp_rate,
        )
        self.delay_correct_hier_0_0 = delay_correct_hier(
            cal_tone_freq=cal_tone_freq,
            mu=0.001,
            samp_rate=samp_rate,
        )
        self.blocks_throttle_0_1 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.from_double(variable_qtgui_chooser_0_1_0), 1000)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_gr_complex*1, variable_qtgui_range_0_0)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, variable_qtgui_range_0)
        self.blocks_complex_to_real_0_1 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.delay_correct_hier_0_0, 'enable_sync'))    
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.delay_correct_hier_0_0_0, 'enable_sync'))    
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0_1, 0))    
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_time_sink_x_0_0, 1))    
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.blocks_complex_to_real_0_1, 0), (self.qtgui_time_sink_x_0_0, 2))    
        self.connect((self.blocks_delay_0, 0), (self.delay_correct_hier_0_0, 0))    
        self.connect((self.blocks_delay_0_0, 0), (self.delay_correct_hier_0_0_0, 0))    
        self.connect((self.blocks_throttle_0_1, 0), (self.blocks_complex_to_real_0_0, 0))    
        self.connect((self.blocks_throttle_0_1, 0), (self.blocks_delay_0, 0))    
        self.connect((self.blocks_throttle_0_1, 0), (self.blocks_delay_0_0, 0))    
        self.connect((self.blocks_throttle_0_1, 0), (self.delay_correct_hier_0_0, 1))    
        self.connect((self.blocks_throttle_0_1, 0), (self.delay_correct_hier_0_0_0, 1))    
        self.connect((self.delay_correct_hier_0_0, 0), (self.blocks_complex_to_real_0, 0))    
        self.connect((self.delay_correct_hier_0_0_0, 0), (self.blocks_complex_to_real_0_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "test_shift_and_measure")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_vec_size(int(2**( numpy.ceil(numpy.log(self.samp_rate/self.cal_tone_freq)/numpy.log(2)))))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0_1.set_sample_rate(self.samp_rate)
        self.delay_correct_hier_0_0.set_samp_rate(self.samp_rate)
        self.delay_correct_hier_0_0_0.set_samp_rate(self.samp_rate)

    def get_cal_tone_freq(self):
        return self.cal_tone_freq

    def set_cal_tone_freq(self, cal_tone_freq):
        self.cal_tone_freq = cal_tone_freq
        self.set_vec_size(int(2**( numpy.ceil(numpy.log(self.samp_rate/self.cal_tone_freq)/numpy.log(2)))))
        self.delay_correct_hier_0_0.set_cal_tone_freq(self.cal_tone_freq)
        self.delay_correct_hier_0_0_0.set_cal_tone_freq(self.cal_tone_freq)

    def get_vec_size(self):
        return self.vec_size

    def set_vec_size(self, vec_size):
        self.vec_size = vec_size

    def get_variable_qtgui_range_0_0(self):
        return self.variable_qtgui_range_0_0

    def set_variable_qtgui_range_0_0(self, variable_qtgui_range_0_0):
        self.variable_qtgui_range_0_0 = variable_qtgui_range_0_0
        self.blocks_delay_0_0.set_dly(self.variable_qtgui_range_0_0)

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0
        self.blocks_delay_0.set_dly(self.variable_qtgui_range_0)

    def get_variable_qtgui_chooser_0_1_0(self):
        return self.variable_qtgui_chooser_0_1_0

    def set_variable_qtgui_chooser_0_1_0(self, variable_qtgui_chooser_0_1_0):
        self.variable_qtgui_chooser_0_1_0 = variable_qtgui_chooser_0_1_0
        self._variable_qtgui_chooser_0_1_0_callback(self.variable_qtgui_chooser_0_1_0)
        self.blocks_message_strobe_0.set_msg(pmt.from_double(self.variable_qtgui_chooser_0_1_0))


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = test_shift_and_measure()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
