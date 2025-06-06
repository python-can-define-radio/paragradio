#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import osmosdr
import time
from gnuradio import qtgui

class psk_tx_loop_gr3_8(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
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

        self.settings = Qt.QSettings("GNU Radio", "psk_tx_loop_gr3_8")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.modulation = modulation = "BPSK"
        self.stel_qpsk = stel_qpsk = digital.constellation_qpsk().base()
        self.stel_dqpsk = stel_dqpsk = digital.constellation_dqpsk().base()
        self.stel_bpsk = stel_bpsk = digital.constellation_bpsk().base()
        self.stel_8psk = stel_8psk = digital.constellation_8psk().base()
        self.stel_16qam = stel_16qam = digital.constellation_16qam().base()
        self.samp_rate = samp_rate = 2e6
        self.if_gain = if_gain = 0
        self.data = data = [0,0]
        self.converted_constellationindex_from_modulation = converted_constellationindex_from_modulation = ["BPSK", "QPSK", "DQPSK", "8PSK", "16QAM"].index(modulation)
        self.center_freq = center_freq = 2.4e9
        self.amplitude = amplitude = 0

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            1024, #size
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            center_freq, #fc
            samp_rate, #bw
            "", #name
            1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + "hackrf=0"
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(center_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(0, 0)
        self.osmosdr_sink_0.set_if_gain(if_gain, 0)
        self.osmosdr_sink_0.set_bb_gain(0, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.digital_constellation_modulator_0_0_0_0_0 = digital.generic_mod(
            constellation=stel_16qam,
            differential=False,
            samples_per_symbol=2,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=False,
            log=False)
        self.digital_constellation_modulator_0_0_0_0 = digital.generic_mod(
            constellation=stel_8psk,
            differential=False,
            samples_per_symbol=2,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=False,
            log=False)
        self.digital_constellation_modulator_0_0_0 = digital.generic_mod(
            constellation=stel_dqpsk,
            differential=False,
            samples_per_symbol=2,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=False,
            log=False)
        self.digital_constellation_modulator_0_0 = digital.generic_mod(
            constellation=stel_qpsk,
            differential=False,
            samples_per_symbol=2,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=False,
            log=False)
        self.digital_constellation_modulator_0 = digital.generic_mod(
            constellation=stel_bpsk,
            differential=False,
            samples_per_symbol=2,
            pre_diff_code=True,
            excess_bw=0.35,
            verbose=False,
            log=False)
        self.blocks_vector_source_x_0_1_0_0 = blocks.vector_source_b(data, True, 1, [])
        self.blocks_vector_source_x_0_1_0 = blocks.vector_source_b(data, True, 1, [])
        self.blocks_vector_source_x_0_1 = blocks.vector_source_b(data, True, 1, [])
        self.blocks_vector_source_x_0_0 = blocks.vector_source_b(data, True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_b(data, True, 1, [])
        self.blocks_selector_0 = blocks.selector(gr.sizeof_gr_complex*1,converted_constellationindex_from_modulation,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(complex(amplitude))



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.blocks_selector_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.digital_constellation_modulator_0_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_0, 0), (self.digital_constellation_modulator_0_0_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_1, 0), (self.digital_constellation_modulator_0_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_1_0, 0), (self.digital_constellation_modulator_0_0, 0))
        self.connect((self.blocks_vector_source_x_0_1_0_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_selector_0, 0))
        self.connect((self.digital_constellation_modulator_0_0, 0), (self.blocks_selector_0, 1))
        self.connect((self.digital_constellation_modulator_0_0_0, 0), (self.blocks_selector_0, 2))
        self.connect((self.digital_constellation_modulator_0_0_0_0, 0), (self.blocks_selector_0, 3))
        self.connect((self.digital_constellation_modulator_0_0_0_0_0, 0), (self.blocks_selector_0, 4))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "psk_tx_loop_gr3_8")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_modulation(self):
        return self.modulation

    def set_modulation(self, modulation):
        self.modulation = modulation
        self.set_converted_constellationindex_from_modulation(["BPSK", "QPSK", "DQPSK", "8PSK", "16QAM"].index(self.modulation))

    def get_stel_qpsk(self):
        return self.stel_qpsk

    def set_stel_qpsk(self, stel_qpsk):
        self.stel_qpsk = stel_qpsk

    def get_stel_dqpsk(self):
        return self.stel_dqpsk

    def set_stel_dqpsk(self, stel_dqpsk):
        self.stel_dqpsk = stel_dqpsk

    def get_stel_bpsk(self):
        return self.stel_bpsk

    def set_stel_bpsk(self, stel_bpsk):
        self.stel_bpsk = stel_bpsk

    def get_stel_8psk(self):
        return self.stel_8psk

    def set_stel_8psk(self, stel_8psk):
        self.stel_8psk = stel_8psk

    def get_stel_16qam(self):
        return self.stel_16qam

    def set_stel_16qam(self, stel_16qam):
        self.stel_16qam = stel_16qam

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        self.osmosdr_sink_0.set_if_gain(self.if_gain, 0)

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
        self.blocks_vector_source_x_0.set_data(self.data, [])
        self.blocks_vector_source_x_0_0.set_data(self.data, [])
        self.blocks_vector_source_x_0_1.set_data(self.data, [])
        self.blocks_vector_source_x_0_1_0.set_data(self.data, [])
        self.blocks_vector_source_x_0_1_0_0.set_data(self.data, [])

    def get_converted_constellationindex_from_modulation(self):
        return self.converted_constellationindex_from_modulation

    def set_converted_constellationindex_from_modulation(self, converted_constellationindex_from_modulation):
        self.converted_constellationindex_from_modulation = converted_constellationindex_from_modulation
        self.blocks_selector_0.set_input_index(self.converted_constellationindex_from_modulation)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.osmosdr_sink_0.set_center_freq(self.center_freq, 0)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude
        self.blocks_multiply_const_vxx_0.set_k(complex(self.amplitude))



def main(top_block_cls=psk_tx_loop_gr3_8, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
