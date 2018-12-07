#encoding: utf-8

from .. import register
from ..base import BranchInstruction


@register(opcode=0XA5)
class IF_ACMPEQ(BranchInstruction):

    def is_branch(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        return left == right


@register(opcode=0XA6)
class IF_ACMPNE(BranchInstruction):

    def is_branch(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        return left != right
