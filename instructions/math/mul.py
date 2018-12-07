#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction


class MUL(NoOperandsInstruction):

    def execute(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.push(left * right)


@register(opcode=0X68)
class IMUL(MUL):
    pass


@register(opcode=0X69)
class LMUL(MUL):
    pass


@register(opcode=0X6A)
class FMUL(MUL):
    pass


@register(opcode=0X6B)
class DMUL(MUL):
    pass
