#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction


@register(opcode=0X88)
class L2I(NoOperandsInstruction):
    def execute(self, frame):
        val = frame.stack.pop()
        frame.stack.push(val)


@register(opcode=0X89)
class L2F(NoOperandsInstruction):
    def execute(self, frame):
        val = frame.stack.pop()
        frame.stack.push(float(val))


@register(opcode=0X8A)
class L2D(NoOperandsInstruction):
    def execute(self, frame):
        val = frame.stack.pop()
        frame.stack.push(float(val))