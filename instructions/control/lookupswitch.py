#encoding: utf-8

from .. import register
from ..base import Instruction


@register(opcode=0XAB)
class LOOKUP_SWITCH(Instruction):

    def __init__(self):
        self.__default_offset = 0
        self.__npairs = 0
        self.__match_offsets = []

    def fetch_operands(self, reader):
        reader.skip_padding()

        self.__default_offset = reader.read_32_byte()
        self.__npairs = reader.read_32_byte()
        self.__match_offsets = self.read_32_bytes(2 * int(self.__npairs))

    def execute(self, frame):
        key = frame.stack.pop()
        offset = self.__default_offset
        for i in range(0, self.__npairs * 2, 2):
            if int(self.__match_offsets[i]) == key:
                offset = self.__match_offsets[i + 1]
                break

        frame.next_pc = frame.thread.pc + self.offset