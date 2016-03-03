#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Mar  3 11:49:06 2016
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from music_spectrum_hier_gui import music_spectrum_hier_gui  # grc-generated hier_block
from optparse import OptionParser
import matlab


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
        self.vec = vec = 3
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 0
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_0_range = Range(-90, 90, 1, 0, 200)
        self._variable_qtgui_range_0_win = RangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, "Angle", "counter_slider", float)
        self.top_layout.addWidget(self._variable_qtgui_range_0_win)
        self.music_spectrum_hier_gui_0 = music_spectrum_hier_gui(
            snapshots=32,
            source_signals=1,
            d=0.5,
        )
        self.top_layout.addWidget(self.music_spectrum_hier_gui_0)
        self.matlab_shift_aoa_cc_0 = matlab.shift_aoa_cc(variable_qtgui_range_0, samp_rate, 0.5, 4)
        self.blocks_vector_source_x_0_0_0 = blocks.vector_source_f((1,1,1,1), True, 4, [])
        self.blocks_vector_source_x_0_0 = blocks.vector_source_f((0,0,0,0), True, 4, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_c((0, 1+1j, 2+2j), True, 1, [])
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.matlab_shift_aoa_cc_0, 3))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.matlab_shift_aoa_cc_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.matlab_shift_aoa_cc_0, 1))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.matlab_shift_aoa_cc_0, 2))    
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.music_spectrum_hier_gui_0, 5))    
        self.connect((self.blocks_vector_source_x_0_0_0, 0), (self.music_spectrum_hier_gui_0, 0))    
        self.connect((self.matlab_shift_aoa_cc_0, 0), (self.music_spectrum_hier_gui_0, 1))    
        self.connect((self.matlab_shift_aoa_cc_0, 1), (self.music_spectrum_hier_gui_0, 2))    
        self.connect((self.matlab_shift_aoa_cc_0, 2), (self.music_spectrum_hier_gui_0, 3))    
        self.connect((self.matlab_shift_aoa_cc_0, 3), (self.music_spectrum_hier_gui_0, 4))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_vec(self):
        return self.vec

    def set_vec(self, vec):
        self.vec = vec

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0
        self.matlab_shift_aoa_cc_0.set_angle(self.variable_qtgui_range_0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)


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
