#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Dec 21 14:10:55 2015
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

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys
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
        self.samp_rate = samp_rate = 1024000
        self.cal_freq = cal_freq = 1000
        self.vec_size = vec_size = samp_rate/cal_freq*2
        self.variable_qtgui_range_0_1 = variable_qtgui_range_0_1 = 50
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 20
        self.points = points = 10000

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_0_1_range = Range(0, 180, 2, 50, 200)
        self._variable_qtgui_range_0_1_win = RangeWidget(self._variable_qtgui_range_0_1_range, self.set_variable_qtgui_range_0_1, "Input_Delay", "counter_slider", int)
        self.top_layout.addWidget(self._variable_qtgui_range_0_1_win)
        self._variable_qtgui_range_0_range = Range(0, 180, 2, 20, 200)
        self._variable_qtgui_range_0_win = RangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, "Input_Delay", "counter_slider", int)
        self.top_layout.addWidget(self._variable_qtgui_range_0_win)
        self.wifius_mode_0_0 = wifius.mode(-100,100,128)
        self.wifius_mode_0 = wifius.mode(-100,100,128)
        self.wifius_measure_phases_0 = wifius.measure_phases(samp_rate, cal_freq, 100, vec_size)
        self.qtgui_time_sink_x_0_0_0_1 = qtgui.time_sink_f(
        	points, #size
        	samp_rate, #samp_rate
        	"Offsets", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0_1.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0_0_1.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_1.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0_1.disable_legend()
        
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
                self.qtgui_time_sink_x_0_0_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_1_win)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_f(
        	points, #size
        	samp_rate, #samp_rate
        	"Offsets", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()
        
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
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.blocks_vector_to_stream_0_0_0_1 = blocks.vector_to_stream(gr.sizeof_int*1, vec_size)
        self.blocks_vector_to_stream_0_0_0 = blocks.vector_to_stream(gr.sizeof_int*1, vec_size)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_vector_0_1_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, vec_size)
        self.blocks_stream_to_vector_0_1_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, vec_size)
        self.blocks_int_to_float_0_2_0 = blocks.int_to_float(1, 1)
        self.blocks_int_to_float_0_2 = blocks.int_to_float(1, 1)
        self.blocks_int_to_float_0_0 = blocks.int_to_float(1, 1)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.blocks_delay_0_1_0 = blocks.delay(gr.sizeof_gr_complex*1, variable_qtgui_range_0)
        self.blocks_delay_0_1 = blocks.delay(gr.sizeof_gr_complex*1, variable_qtgui_range_0_1)
        self.blocks_complex_to_real_0_1_0 = blocks.complex_to_real(vec_size)
        self.blocks_complex_to_real_0_1 = blocks.complex_to_real(vec_size)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, cal_freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_complex_to_real_0_1, 0), (self.wifius_measure_phases_0, 0))    
        self.connect((self.blocks_complex_to_real_0_1_0, 0), (self.wifius_measure_phases_0, 1))    
        self.connect((self.blocks_delay_0_1, 0), (self.blocks_stream_to_vector_0_1_0, 0))    
        self.connect((self.blocks_delay_0_1_0, 0), (self.blocks_stream_to_vector_0_1_0_1, 0))    
        self.connect((self.blocks_int_to_float_0, 0), (self.qtgui_time_sink_x_0_0_0, 1))    
        self.connect((self.blocks_int_to_float_0_0, 0), (self.qtgui_time_sink_x_0_0_0_1, 1))    
        self.connect((self.blocks_int_to_float_0_2, 0), (self.qtgui_time_sink_x_0_0_0, 0))    
        self.connect((self.blocks_int_to_float_0_2_0, 0), (self.qtgui_time_sink_x_0_0_0_1, 0))    
        self.connect((self.blocks_stream_to_vector_0_1_0, 0), (self.blocks_complex_to_real_0_1, 0))    
        self.connect((self.blocks_stream_to_vector_0_1_0_1, 0), (self.blocks_complex_to_real_0_1_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_delay_0_1, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_delay_0_1_0, 0))    
        self.connect((self.blocks_vector_to_stream_0_0_0, 0), (self.blocks_int_to_float_0_0, 0))    
        self.connect((self.blocks_vector_to_stream_0_0_0, 0), (self.wifius_mode_0_0, 0))    
        self.connect((self.blocks_vector_to_stream_0_0_0_1, 0), (self.blocks_int_to_float_0_2_0, 0))    
        self.connect((self.blocks_vector_to_stream_0_0_0_1, 0), (self.wifius_mode_0, 0))    
        self.connect((self.wifius_measure_phases_0, 1), (self.blocks_vector_to_stream_0_0_0, 0))    
        self.connect((self.wifius_measure_phases_0, 0), (self.blocks_vector_to_stream_0_0_0_1, 0))    
        self.connect((self.wifius_mode_0, 0), (self.blocks_int_to_float_0_2, 0))    
        self.connect((self.wifius_mode_0_0, 0), (self.blocks_int_to_float_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_vec_size(self.samp_rate/self.cal_freq*2)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_0_1.set_samp_rate(self.samp_rate)

    def get_cal_freq(self):
        return self.cal_freq

    def set_cal_freq(self, cal_freq):
        self.cal_freq = cal_freq
        self.set_vec_size(self.samp_rate/self.cal_freq*2)
        self.analog_sig_source_x_0.set_frequency(self.cal_freq)

    def get_vec_size(self):
        return self.vec_size

    def set_vec_size(self, vec_size):
        self.vec_size = vec_size

    def get_variable_qtgui_range_0_1(self):
        return self.variable_qtgui_range_0_1

    def set_variable_qtgui_range_0_1(self, variable_qtgui_range_0_1):
        self.variable_qtgui_range_0_1 = variable_qtgui_range_0_1
        self.blocks_delay_0_1.set_dly(self.variable_qtgui_range_0_1)

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0
        self.blocks_delay_0_1_0.set_dly(self.variable_qtgui_range_0)

    def get_points(self):
        return self.points

    def set_points(self, points):
        self.points = points


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_block()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
