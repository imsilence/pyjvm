#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction


@register(opcode=0X59)
class DUP(NoOperandsInstruction):

    def execute(self, frame):
        value = frame.stack.pop()
        frame.stack.push(value)
        frame.stack.push(value)


@register(opcode=0X5A)
class DUP_X1(NoOperandsInstruction):

    def execute(self, frame):
        value1 = frame.stack.pop()
        value2 = frame.stack.pop()
        frame.stack.push(value1)
        frame.stack.push(value2)
        frame.stack.push(value1)


@register(opcode=0X5B)
class DUP_X2(NoOperandsInstruction):

    def execute(self, frame):
        value1 = frame.stack.pop()
        value2 = frame.stack.pop()
        value3 = frame.stack.pop()
        frame.stack.push(value1)
        frame.stack.push(value3)
        frame.stack.push(value2)
        frame.stack.push(value1)


@register(opcode=0X5C)
class DUP2(NoOperandsInstruction):

    def execute(self, frame):
        value1 = frame.stack.pop()
        value2 = frame.stack.pop()
        frame.stack.push(value2)
        frame.stack.push(value1)
        frame.stack.push(value2)
        frame.stack.push(value1)


@register(opcode=0X5D)
class DUP2_X1(NoOperandsInstruction):

    def execute(self, frame):
        value1 = frame.stack.pop()
        value2 = frame.stack.pop()
        value3 = frame.stack.pop()
        frame.stack.push(value2)
        frame.stack.push(value1)
        frame.stack.push(value3)
        frame.stack.push(value2)
        frame.stack.push(value1)


@register(opcode=0X5E)
class DUP2_X2(NoOperandsInstruction):

    def execute(self, frame):
        value1 = frame.stack.pop()
        value2 = frame.stack.pop()
        value3 = frame.stack.pop()
        value4 = frame.stack.pop()
        frame.stack.push(value2)
        frame.stack.push(value1)
        frame.stack.push(value4)
        frame.stack.push(value3)
        frame.stack.push(value2)
        frame.stack.push(value1)