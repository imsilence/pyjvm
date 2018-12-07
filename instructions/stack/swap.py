#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction


@register(opcode=0X5F)
class SWAP(NoOperandsInstruction):

    def execute(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.push(right)
        frame.stack.push(left)