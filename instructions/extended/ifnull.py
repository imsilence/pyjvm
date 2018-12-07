#encoding: utf-8

from .. import register
from ..base import BranchInstruction


@register(opcode=0XC6)
class IFNULL(BranchInstruction):

    def is_branch(self, frame):
        return frame.stack.pop() is None
