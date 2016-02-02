#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Calibration Example
# Author: Travis Collins
# Description: WiFiUS Project
# Generated: Sun Jan 31 16:52:36 2016
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
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import time


class calibration_example_gui_2x(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "calibration_example_gui_2x")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.speed_of_light = speed_of_light = 299792458
        self.antenna_spacing = antenna_spacing = 0.1
        self.samp_rate = samp_rate = 100000000/64
        self.gain_rx = gain_rx = 0
        self.center_freq = center_freq = speed_of_light/(2*antenna_spacing)
        self.cal_freq = cal_freq = 1024

        ##################################################
        # Blocks
        ##################################################
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

        s1 = 0;
        s2 = 5;
        s3 = 700;
        s4 = 640;

        cmd_time1 = cmd_time + uhd.time_spec_t(0);
        cmd_time2 = cmd_time + uhd.time_spec_t(s2/samp_rate);
        cmd_time3 = cmd_time + uhd.time_spec_t(s3/samp_rate);
        cmd_time4 = cmd_time + uhd.time_spec_t(s4/samp_rate);

        self.uhd_usrp_source_0_0_0.set_command_time(cmd_time1,0)
        self.uhd_usrp_source_0_0_0.set_command_time(cmd_time2,1)
        self.uhd_usrp_source_0_0_0.set_command_time(cmd_time3,2)
        self.uhd_usrp_source_0_0_0.set_command_time(cmd_time4,3)

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
        self.blocks_complex_to_real_1_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_1 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0_0 = blocks.complex_to_real(1)
        self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, cal_freq, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.uhd_usrp_sink_0_0, 0))
        self.connect((self.blocks_complex_to_real_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_complex_to_real_0_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_complex_to_real_1, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_complex_to_real_1_0, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.uhd_usrp_source_0_0_0, 0), (self.blocks_complex_to_real_0, 0))
        self.connect((self.uhd_usrp_source_0_0_0, 2), (self.blocks_complex_to_real_0_0, 0))
        self.connect((self.uhd_usrp_source_0_0_0, 1), (self.blocks_complex_to_real_1, 0))
        self.connect((self.uhd_usrp_source_0_0_0, 3), (self.blocks_complex_to_real_1_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "calibration_example_gui_2x")
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

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
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


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = calibration_example_gui_2x()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
