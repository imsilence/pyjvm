#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction


class ADD(NoOperandsInstruction):

    def execute(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.push(left + right)


@register(opcode=0X60)
class IADD(ADD):
    pass


@register(opcode=0X61)
class LADD(ADD):
    pass


@register(opcode=0X62)
class FADD(ADD):
    pass


@register(opcode=0X63)
class DADD(ADD):
    pass
