#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction

class OR(NoOperandsInstruction):

    def execute(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.push(left | right)


@register(opcode=0X80)
class IOR(OR):
    pass


@register(opcode=0X81)
class LOR(OR):
    pass