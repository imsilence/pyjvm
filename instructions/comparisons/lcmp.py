#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction

@register(opcode=0X94)
class LCMP(NoOperandsInstruction):

    def execute(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()

        if left > right:
            value = 1
        elif left == right:
            value = 0
        else:
            value = -1

        frame.stack.push(value)