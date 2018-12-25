#encoding: utf-8

from .. import register
from ..base import Index16Instruction


@register(opcode=0XB6)
class INVOKE_SPECIAL(Index16Instruction):

    def execute(self, frame):
        constant_pool = frame.method.clazz.constant_pool
        method_ref = constant_pool[self.index]
        if method_ref.name == 'println':
            print(frame.stack.pop())
            print(frame.stack.pop())