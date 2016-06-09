#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

import numpy
import pmt
from gnuradio import gr
from gnuradio import blocks

class selector_control(gr.hier_block2):
    """A hier2 block with 1 input and M outputs, where data is only forwarded through input 1 to output m."""
    def __init__(self, item_size, num_outputs, default_output):
        """
        Selector constructor.
        Args:
            item_size: the size of the gr data stream in bytes
            num_inputs: the number of inputs (integer)
            num_outputs: the number of outputs (integer)
            input_index: the index for the source data
            output_index: the index for the destination data
        """
        gr.hier_block2.__init__(
            self, 'selector',
            gr.io_signature(1, 1, item_size),
            gr.io_signature(num_outputs, num_outputs, item_size),
        )
        num_inputs = 1
        # Terminator blocks for unused inputs and outputs
        self.input_terminators = [blocks.null_sink(item_size) for i in range(num_inputs)]
        self.output_terminators = [blocks.head(item_size, 0) for i in range(num_outputs)]
        self.copy = blocks.copy(item_size)
        # Connections
        for i in range(num_inputs): self.connect((self, i), self.input_terminators[i])
        for i in range(num_outputs): self.connect(blocks.null_source(item_size), self.output_terminators[i], (self, i))
        # Set parameters
        self.num_outputs = num_outputs
        self.input_index = 0
        self.output_index = default_output
        # Register the message port
        self.message_port_register_hier_in("selection")
        self.mb = message_receiver(self);
        # Connect message port
        self.msg_connect(self, "selection", self.mb,"selection")
        # Connect default
        self._connect_current()

    def _indexes_valid(self):
        """
        Are the input and output indexes within range of the number of inputs and outputs?
        Returns:
            true if input index and output index are in range
        """
        return self.output_index in range(self.num_outputs)

    def _connect_current(self):
        """If the input and output indexes are valid:
        disconnect the blocks at the input and output index from their terminators,
        and connect them to one another. Then connect the terminators to one another."""
        if self._indexes_valid():
            self.disconnect((self, self.input_index), self.input_terminators[self.input_index])
            self.disconnect(self.output_terminators[self.output_index], (self, self.output_index))
            self.connect((self, self.input_index), self.copy)
            self.connect(self.copy, (self, self.output_index))
            self.connect(self.output_terminators[self.output_index], self.input_terminators[self.input_index])

    def _disconnect_current(self):
        """If the input and output indexes are valid:
        disconnect the blocks at the input and output index from one another,
        and the terminators at the input and output index from one another.
        Reconnect the blocks to the terminators."""
        if self._indexes_valid():
            self.disconnect((self, self.input_index), self.copy)
            self.disconnect(self.copy, (self, self.output_index))
            self.disconnect(self.output_terminators[self.output_index], self.input_terminators[self.input_index])
            self.connect((self, self.input_index), self.input_terminators[self.input_index])
            self.connect(self.output_terminators[self.output_index], (self, self.output_index))

    def set_output_index(self, output_index):
        """
        Change the block to the new output index if the index changed.
        Args:
            output_index: the new output index
        """
        if self.output_index != output_index:
            self.lock()
            self._disconnect_current()
            self.output_index = output_index
            self._connect_current()
            self.unlock()

    def handle_msg(self, msg_pmt):
        """ Receiver a int on the input port, and print it out. """
        print "Message Handler Called"
        # Collect message, convert to Python format:
        newIndex = pmt.to_long(msg_pmt)
        print "Got New Message: "+str(newIndex)
        print id(self)
        # Change output to new from message
        self.set_output_index(newIndex)

class message_receiver(gr.basic_block):
    """ Receiver Message and call parent block callback """
    def __init__(self,parent):
        gr.basic_block.__init__(self,
            name="message_receiver",
            in_sig=[], # No streaming ports!
            out_sig=[])
        # Register the message port
        self.parent = parent
        self.message_port_register_in(pmt.intern('selection'))
        self.set_msg_handler(pmt.intern('selection'), self.parent.handle_msg)

    def handler(self, msg_pmt):
        print "OTHER: Message Handler Called"
