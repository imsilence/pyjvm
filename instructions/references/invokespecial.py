#encoding: utf-8

from .. import register
from ..base import Index16Instruction
from ..exceptions import InstructionException
from .invoke import InvokeMixin
from rtda.heap import MethodRef


@register(opcode=0XB7)
class INVOKE_SPECIAL(InvokeMixin, Index16Instruction):

    def execute(self, frame):
        current_class = frame.method.clazz
        method_ref = current_class.constant_pool[self.index]
        clazz = method_ref.clazz
        method = method_ref.method

        if method.name == '<init>' and method.clazz != clazz:
            raise InstructionException('method {0}.{1} not found'.format(method.clazz.name, method.name))

        if method.is_static:
            raise InstructionException('method {0}.{1} is static'.format(method.clazz.name, method.name))

        ref = frame.stack.top(method.signature.var_count)
        if ref is None:
            raise InstructionException('ref {0}.{1} None'.format(method.clazz.name, method.name))

        if method.is_protected and method.clazz.is_superclass(current_class) and \
            method.clazz.package_name != current_class.package_name and \
            ref.clazz != current_class and not ref.clazz.is_subclass(current_class):
            raise InstructionException('class {0} not vist method {1}.{2} access'.format(current_class.name, method.clazz.name, method.name))

        if current_class.is_super and clazz.is_superclass(current_class) and \
            method.name != '<init>':
            method = MethodRef.lookup(current_class.super_class, method.name, method.descriptor)

        if method is None or method.is_abstract:
            raise InstructionException('method {0}.{1} is abstract'.format(method.clazz.name, method.name))

        self.invoke_method(frame, method)