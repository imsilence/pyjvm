#encoding: utf-8

from .. import register
from ..base import Instruction


@register(opcode=0XAA)
class TABLE_SWITCH(Instruction):

    def __init__(self):
        self.__default_offset = 0
        self.__low = 0
        self.__high = 0
        self.__jump_offsets = []

    def fetch_operands(self, reader):
        reader.skip_padding()

        self.__default_offset = reader.read_32_byte()
        self.__low = reader.read_32_byte()
        self.__high = reader.read_32_byte()

        count = int(self.__high) - int(self.__low) + 1

        self.__jump_offsets = self.read_32_bytes(count)

    def execute(self, frame):
        index = frame.stack.pop()
        offset = self.__default_offset
        if index >= int(self.__low) and int(index <= self.__high):
            offset = self.__jump_offsets[index - int(self.__low)]

        frame.next_pc = frame.thread.pc + self.offset