#!/usr/bin/env python2
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Jan 25 08:46:02 2016
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
from correct_gains_hier import correct_gains_hier  # grc-generated hier_block
from delay_correct_hier import delay_correct_hier  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt
import wifius


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, cal_freq=1, samp_rate=1):
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
        # Parameters
        ##################################################
        self.cal_freq = cal_freq
        self.samp_rate = samp_rate

        ##################################################
        # Blocks
        ##################################################
        self.wifius_correct_input_0_1 = wifius.correct_input(1)
        self.wifius_correct_input_0_0 = wifius.correct_input(1)
        self.wifius_correct_input_0 = wifius.correct_input(1)
        self.delay_correct_hier_0_0_0 = delay_correct_hier(
            cal_tone_freq=cal_freq,
            mu=0.0001,
            samp_rate=samp_rate,
        )
        self.delay_correct_hier_0_0 = delay_correct_hier(
            cal_tone_freq=cal_freq,
            mu=0.0001,
            samp_rate=samp_rate,
        )
        self.delay_correct_hier_0 = delay_correct_hier(
            cal_tone_freq=cal_freq,
            mu=0.0001,
            samp_rate=samp_rate,
        )
        self.correct_gains_hier_0 = correct_gains_hier(
            cal_tone_freq=cal_freq,
            samp_rate_0=samp_rate,
        )
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_copy_0 = blocks.copy(gr.sizeof_gr_complex*1)
        self.blocks_copy_0.set_enabled(True)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.delay_correct_hier_0, 'offset'), (self.wifius_correct_input_0, 'set_delay'))    
        self.msg_connect((self.delay_correct_hier_0_0, 'offset'), (self.wifius_correct_input_0_0, 'set_delay'))    
        self.msg_connect((self.delay_correct_hier_0_0_0, 'offset'), (self.wifius_correct_input_0_1, 'set_delay'))    
        self.msg_connect((self, 'in'), (self.correct_gains_hier_0, 'Trigger'))    
        self.msg_connect((self, 'in'), (self.delay_correct_hier_0, 'enable_sync'))    
        self.msg_connect((self, 'in'), (self.delay_correct_hier_0_0, 'enable_sync'))    
        self.msg_connect((self, 'in'), (self.delay_correct_hier_0_0_0, 'enable_sync'))    
        self.connect((self.blocks_copy_0, 0), (self, 0))    
        self.connect((self.correct_gains_hier_0, 0), (self.delay_correct_hier_0, 1))    
        self.connect((self.correct_gains_hier_0, 1), (self.delay_correct_hier_0, 0))    
        self.connect((self.correct_gains_hier_0, 0), (self.delay_correct_hier_0_0, 1))    
        self.connect((self.correct_gains_hier_0, 2), (self.delay_correct_hier_0_0, 0))    
        self.connect((self.correct_gains_hier_0, 0), (self.delay_correct_hier_0_0_0, 1))    
        self.connect((self.correct_gains_hier_0, 3), (self.delay_correct_hier_0_0_0, 0))    
        self.connect((self.delay_correct_hier_0, 0), (self.blocks_null_sink_0, 0))    
        self.connect((self.delay_correct_hier_0_0, 0), (self.blocks_null_sink_0, 1))    
        self.connect((self.delay_correct_hier_0_0_0, 0), (self.blocks_null_sink_0, 2))    
        self.connect((self, 0), (self.blocks_copy_0, 0))    
        self.connect((self, 0), (self.correct_gains_hier_0, 0))    
        self.connect((self, 1), (self.correct_gains_hier_0, 1))    
        self.connect((self, 2), (self.correct_gains_hier_0, 2))    
        self.connect((self, 3), (self.correct_gains_hier_0, 3))    
        self.connect((self, 1), (self.wifius_correct_input_0, 0))    
        self.connect((self, 2), (self.wifius_correct_input_0_0, 0))    
        self.connect((self, 3), (self.wifius_correct_input_0_1, 0))    
        self.connect((self.wifius_correct_input_0, 0), (self, 1))    
        self.connect((self.wifius_correct_input_0_0, 0), (self, 2))    
        self.connect((self.wifius_correct_input_0_1, 0), (self, 3))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_cal_freq(self):
        return self.cal_freq

    def set_cal_freq(self, cal_freq):
        self.cal_freq = cal_freq
        self.correct_gains_hier_0.set_cal_tone_freq(self.cal_freq)
        self.delay_correct_hier_0.set_cal_tone_freq(self.cal_freq)
        self.delay_correct_hier_0_0.set_cal_tone_freq(self.cal_freq)
        self.delay_correct_hier_0_0_0.set_cal_tone_freq(self.cal_freq)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.correct_gains_hier_0.set_samp_rate_0(self.samp_rate)
        self.delay_correct_hier_0.set_samp_rate(self.samp_rate)
        self.delay_correct_hier_0_0.set_samp_rate(self.samp_rate)
        self.delay_correct_hier_0_0_0.set_samp_rate(self.samp_rate)


if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--cal-freq", dest="cal_freq", type="eng_float", default=eng_notation.num_to_str(1),
        help="Set Calibration Tone Freq [default=%default]")
    parser.add_option("", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(1),
        help="Set Sample Rate [default=%default]")
    (options, args) = parser.parse_args()
    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = top_block(cal_freq=options.cal_freq, samp_rate=options.samp_rate)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None  # to clean up Qt widgets
