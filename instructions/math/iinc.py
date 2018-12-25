#encoding: utf-8

from .. import register
from ..base import Instruction

@register(opcode=0X84)
class IINC(Instruction):

    def __init__(self):
        self.__index = 0
        self.__const = 0

    def fetch_operands(self, reader):
        self.__index = int(reader.read_8_byte())
        self.__const = reader.read_8_byte().int()

    def execute(self, frame):
        frame.vars[self.__index] += self.__const

