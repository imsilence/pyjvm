#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction

class AND(NoOperandsInstruction):

    def execute(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.push(left & right)


@register(opcode=0X7E)
class IAND(AND):
    pass


@register(opcode=0X7F)
class LAND(AND):
    pass