#encoding: utf-8

from .. import register
from ..base import Index16Instruction
from ..exceptions import InstructionException
from .invoke import Invoke


@register(opcode=0XB8)
class INVOKE_STATIC(Invoke, Index16Instruction):

    def execute(self, frame):
        clazz = frame.method.clazz
        method = clazz.constant_pool[self.index].method
        if not method.is_static:
            raise InstructionException('method {0}.{1} is not static'.format(clazz.name, method.name))

        self.invoke_method(frame, method)