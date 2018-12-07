#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction


@register(opcode=0X8B)
class F2I(NoOperandsInstruction):
    def execute(self, frame):
        val = frame.stack.pop()
        frame.stack.push(int(val))


@register(opcode=0X8C)
class F2L(NoOperandsInstruction):
    def execute(self, frame):
        val = frame.stack.pop()
        frame.stack.push(int(val))


@register(opcode=0X8D)
class F2D(NoOperandsInstruction):
    def execute(self, frame):
        val = frame.stack.pop()
        frame.stack.push(val)