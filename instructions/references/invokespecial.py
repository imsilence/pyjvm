#encoding: utf-8

from .. import register
from ..base import Index16Instruction


@register(opcode=0XB7)
class INVOKE_SPECIAL(Index16Instruction):

    def execute(self, frame):
        frame.stack.pop()