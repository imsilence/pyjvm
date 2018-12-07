#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction


@register(opcode=0X85)
class I2L(NoOperandsInstruction):
    def execute(self, frame):
        val = frame.stack.pop()
        frame.stack.push(val)


@register(opcode=0X86)
class I2F(NoOperandsInstruction):
    def execute(self, frame):
        val = frame.stack.pop()
        frame.stack.push(float(val))


@register(opcode=0X87)
class I2D(NoOperandsInstruction):
    def execute(self, frame):
        val = frame.stack.pop()
        frame.stack.push(float(val))


@register(opcode=0X91)
class I2B(NoOperandsInstruction):
    def execute(self, frame):
        val = frame.stack.pop()
        frame.stack.push(val & 0XF)


@register(opcode=0X92)
class I2C(NoOperandsInstruction):
    def execute(self, frame):
        val = frame.stack.pop()
        frame.stack.push(val & 0XFF)


@register(opcode=0X93)
class I2S(NoOperandsInstruction):
    def execute(self, frame):
        val = frame.stack.pop()
        frame.stack.push(val & 0XFF)