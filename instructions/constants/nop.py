#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction


@register(opcode=0X00)
class NOP(NoOperandsInstruction):

    def execute(self, frame):
        pass
