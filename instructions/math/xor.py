#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction

class XOR(NoOperandsInstruction):

    def execute(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.push(left ^ right)


@register(opcode=0X82)
class IXOR(XOR):
    pass


@register(opcode=0X83)
class LXOR(XOR):
    pass