#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction


@register(opcode=0X57)
class POP(NoOperandsInstruction):

    def execute(self, frame):
        frame.stack.pop()


@register(opcode=0X58)
class POP2(NoOperandsInstruction):

    def execute(self, frame):
        frame.stack.pop()
        frame.stack.pop()