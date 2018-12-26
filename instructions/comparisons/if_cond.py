#encoding: utf-8

from .. import register
from ..base import BranchInstruction

@register(opcode=0X99)
class IFEQ(BranchInstruction):

    def is_branch(self, frame):
        return frame.stack.pop() != 0


@register(opcode=0X9A)
class IFNE(BranchInstruction):

    def is_branch(self, frame):
        return frame.stack.pop() != 0


@register(opcode=0X9B)
class IFLT(BranchInstruction):

    def is_branch(self, frame):
        return frame.stack.pop() < 0


@register(opcode=0X9C)
class IFGE(BranchInstruction):

    def is_branch(self, frame):
        return frame.stack.pop() >= 0


@register(opcode=0X9D)
class IFGT(BranchInstruction):

    def is_branch(self, frame):
        return frame.stack.pop() > 0


@register(opcode=0X9E)
class IFLE(BranchInstruction):

    def is_branch(self, frame):
        return frame.stack.pop() <= 0



