#encoding: utf-8

from .. import register
from ..base import Instruction


class IPUSHInstruction(Instruction):
    def __init__(self):
        self.__value = 0

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def execute(self, frame):
        frame.stack.push(self.value)


@register(opcode=0X10)
class BIPUSH(IPUSHInstruction):
    def fetch_operands(self, reader):
        self.value = reader.read_8_byte().int()


@register(opcode=0X11)
class SIPUSH(IPUSHInstruction):
    def fetch_operands(self, reader):
        self.value = reader.read_16_byte().int()