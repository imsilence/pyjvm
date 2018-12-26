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

        ref = frame.stack.top(len(method.signature.param_types))
        if ref is None:
            raise InstructionException('ref {0}.{1} None'.format(method.clazz.name, method.name))

        if method.is_protected and method.clazz.is_superclass(current_clazz) and \
            method.clazz.package_name != current_clazz.package_name and \
            ref.clazz.is_subclass(current_clazz):
            raise InstructionException('class {0} not vist method {1}.{2} access'.format(current_clazz.name, method.clazz.name, method.name))