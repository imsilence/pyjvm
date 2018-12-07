#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction

class DIV(NoOperandsInstruction):

    def execute(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.push(left / right)


@register(opcode=0X6C)
class IDIV(DIV):
    pass


@register(opcode=0X6D)
class LDIV(DIV):
    pass


@register(opcode=0X6E)
class FDIV(DIV):
    pass


@register(opcode=0X6F)
class DDIV(DIV):
    pass