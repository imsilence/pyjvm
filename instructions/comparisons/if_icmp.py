#encoding: utf-8

from .. import register
from ..base import BranchInstruction


@register(opcode=0X9F)
class IF_ICMPEQ(BranchInstruction):

    def is_branch(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        return right == left


@register(opcode=0XA0)
class IF_ICMPNE(BranchInstruction):

    def is_branch(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        return right != left


@register(opcode=0XA1)
class IF_ICMPLT(BranchInstruction):

    def is_branch(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        return left < right


@register(opcode=0XA2)
class IF_ICMPGE(BranchInstruction):

    def is_branch(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        return left >= right


@register(opcode=0XA3)
class IF_ICMPGT(BranchInstruction):

    def is_branch(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        return left > right


@register(opcode=0XA4)
class IF_ICMPLE(BranchInstruction):

    def is_branch(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        return left <= right



