#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction


class SHL(NoOperandsInstruction):

    def execute(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.push(left << right)


class SHR(NoOperandsInstruction):

    def execute(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.push(left >> right)


@register(opcode=0X78)
class ISHL(SHL):
    pass


@register(opcode=0X79)
class LSHL(SHL):
    pass


@register(opcode=0X7A)
class ISHR(SHR):
    pass


@register(opcode=0X7B)
class LSHR(SHR):
    pass


@register(opcode=0X7C)
class IUSHR(NoOperandsInstruction):

    def execute(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.push((left & 0XFFFFFFFF) >> right)


@register(opcode=0X7D)
class LUSHR(NoOperandsInstruction):
    def execute(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.push((left & 0XFFFFFFFFFFFFFFFF) >> right)