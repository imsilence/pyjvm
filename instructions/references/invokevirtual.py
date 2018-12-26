#encoding: utf-8

from .. import register
from ..base import Index16Instruction
from ..exceptions import InstructionException
from .invoke import Invoke
from rtda.heap import MethodRef

@register(opcode=0XB6)
class INVOKE_VIRTUAL(Invoke, Index16Instruction):

    def execute(self, frame):
        current_clazz = frame.method.clazz
        method_ref = current_clazz.constant_pool[self.index]
        method = method_ref.method
        if method.is_static:
            raise InstructionException('method {0}.{1} is static'.format(method.clazz.name, method.name))

        ref = frame.stack.top(method.signature.var_count)
        print(method.clazz.name, method.name)
        if ref is None:
            if method_ref.name == 'println':
                print('-' * 10)
                print(method_ref.descriptor)
                print(frame.stack.pop())
                print(frame.stack.pop())
                return
            raise InstructionException('ref {0}.{1} None'.format(method.clazz.name, method.name))

        if method.is_protected and method.clazz.is_superclass(current_clazz) and \
            method.clazz.package_name != current_clazz.package_name and \
            ref.clazz != current_clazz and not ref.clazz.is_subclazz(current_clazz):
            raise InstructionException('class {0} not vist method {1}.{2} access'.format(current_clazz.name, method.clazz.name, method.name))

        method = MethodRef.lookup(ref.clazz, method_ref.name, method_ref.descriptor)

        if method is None or method.is_abstract:
            raise InstructionException('method {0}.{1} is abstract'.format(method.clazz.name, method.name))

        self.invoke_method(frame, method)