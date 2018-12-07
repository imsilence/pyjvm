#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction


@register(opcode=0X8E)
class D2I(NoOperandsInstruction):
    def execute(self, frame):
        val = frame.stack.pop()
        frame.stack.push(int(val))


@register(opcode=0X8F)
class D2L(NoOperandsInstruction):
    def execute(self, frame):
        val = frame.stack.pop()
        frame.stack.push(int(val))


@register(opcode=0X90)
class D2F(NoOperandsInstruction):
    def execute(self, frame):
        val = frame.stack.pop()
        frame.stack.push(val)