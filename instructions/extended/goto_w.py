#encoding: utf-8

from .. import register
from ..control.goto import GOTO


@register(opcode=0XC8)
class GOTO_W(GOTO):

    def fetch_operands(self, reader):
        self.__offset = reader.read_32_byte()
