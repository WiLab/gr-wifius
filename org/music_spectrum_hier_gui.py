# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: MuSIC Spectrum GUI
# Author: Travis Collins
# Generated: Fri Mar  4 10:46:47 2016
##################################################

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.filter import firdes
import math
import sip
import wifius


class music_spectrum_hier_gui(gr.hier_block2, Qt.QWidget):

    def __init__(self, d=0.5, snapshots=4096, source_signals=1):
        gr.hier_block2.__init__(
            self, "MuSIC Spectrum GUI",
            gr.io_signaturev(6, 6, [gr.sizeof_float*4, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_gr_complex*1, gr.sizeof_float*4]),
            gr.io_signature(0, 0, 0),
        )

        Qt.QWidget.__init__(self)
        self.top_layout = Qt.QVBoxLayout()
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)
        self.setLayout(self.top_layout)

        ##################################################
        # Parameters
        ##################################################
        self.d = d
        self.snapshots = snapshots
        self.source_signals = source_signals

        ##################################################
        # Variables
        ##################################################
        self.vec = vec = 3
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.wifius_gen_music_spectrum_vcvf_0 = wifius.gen_music_spectrum_vcvf(4, source_signals, -90, 90, 1, d, snapshots)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            180,
            -90,
            1.0,
            "Offset",
            "dB",
            "MuSIC Spectrum",
            1 # Number of inputs
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis(-140, 10)
        self.qtgui_vector_sink_f_0.enable_autoscale(True)
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
        self.top_layout.addWidget(self._qtgui_vector_sink_f_0_win)
        self.blocks_stream_to_vector_0_2 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, snapshots)
        self.blocks_stream_to_vector_0_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, snapshots)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, snapshots)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, snapshots)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_stream_to_vector_0, 0), (self.wifius_gen_music_spectrum_vcvf_0, 2))    
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.wifius_gen_music_spectrum_vcvf_0, 3))    
        self.connect((self.blocks_stream_to_vector_0_1, 0), (self.wifius_gen_music_spectrum_vcvf_0, 4))    
        self.connect((self.blocks_stream_to_vector_0_2, 0), (self.wifius_gen_music_spectrum_vcvf_0, 5))    
        self.connect((self, 0), (self.wifius_gen_music_spectrum_vcvf_0, 0))    
        self.connect((self, 1), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self, 2), (self.blocks_stream_to_vector_0_0, 0))    
        self.connect((self, 3), (self.blocks_stream_to_vector_0_1, 0))    
        self.connect((self, 4), (self.blocks_stream_to_vector_0_2, 0))    
        self.connect((self, 5), (self.wifius_gen_music_spectrum_vcvf_0, 1))    
        self.connect((self.wifius_gen_music_spectrum_vcvf_0, 0), (self.qtgui_vector_sink_f_0, 0))    

    def get_d(self):
        return self.d

    def set_d(self, d):
        self.d = d

    def get_snapshots(self):
        return self.snapshots

    def set_snapshots(self, snapshots):
        self.snapshots = snapshots

    def get_source_signals(self):
        return self.source_signals

    def set_source_signals(self, source_signals):
        self.source_signals = source_signals

    def get_vec(self):
        return self.vec

    def set_vec(self, vec):
        self.vec = vec

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
