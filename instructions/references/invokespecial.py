#encoding: utf-8

from .. import register
from ..base import Index16Instruction
from ..exceptions import InstructionException
from .invoke import Invoke


@register(opcode=0XB7)
class INVOKE_SPECIAL(Invoke):

    def execute(self, frame):
        current_clazz = frame.method.clazz
        method_ref = current_clazz.constant_pool[self.index]
        clazz = method_ref.clazz
        method = method_ref.method

        if method.name == '<init>' and method.clazz != clazz:
            raise InstructionException('method {0}.{1} not found'.format(method.clazz.name, method.name))

        if method.is_static:
            raise InstructionException('method {0}.{1} is static'.format(method.clazz.name, method.name))

        frame.stack.
        raise InstructionException('method {0}.{1} is static'.format(method.clazz.name, method.name))