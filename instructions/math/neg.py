#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction


class NEG(NoOperandsInstruction):

    def execute(self, frame):
        value = frame.stack.pop()
        frame.stack.push(-value)


@register(opcode=0X74)
class INEG(NEG):
    pass


@register(opcode=0X75)
class LNEG(NEG):
    pass


@register(opcode=0X77)
class FNEG(NEG):
    pass


@register(opcode=0X76)
class DNEG(NEG):
    pass
