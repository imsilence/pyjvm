#encoding: utf-8

from .. import register
from ..base import BranchInstruction


@register(opcode=0XA7)
class GOTO(BranchInstruction):

    def is_branch(self, frame):
        return True
