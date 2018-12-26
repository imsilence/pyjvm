#encoding: utf-8

from .. import register
from ..base import Index8Instruction


@register(opcode=0X12)
class LDC(Index8Instruction):

    def execute(self, frame):
        constant_pool = frame.method.clazz.constant_pool
        value = constant_pool[self.index]
        frame.stack.push(value)