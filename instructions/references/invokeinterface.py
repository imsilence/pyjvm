#encoding: utf-8

from .. import register
from ..base import Index16Instruction


@register(opcode=0XB9)
class INVOKE_INTERFACE(Index16Instruction):

    def execute(self, frame):
        frame.stack.pop()