#encoding: utf-8

from .. import register
from ..base import Index16Instruction
from ..exceptions import InstructionException
from .invoke import InvokeMixin
from rtda.heap import MethodRef, StringFactory

@register(opcode=0XB6)
class INVOKE_VIRTUAL(InvokeMixin, Index16Instruction):

    def execute(self, frame):
        current_class = frame.method.clazz
        method_ref = current_class.constant_pool[self.index]
        method = method_ref.method
        if method.is_static:
            raise InstructionException('method {0}.{1} is static'.format(method.clazz.name, method.name))

        ref = frame.stack.top(method.signature.var_count)
        if ref is None:
            # if method_ref.name in ['println', 'print']:
            #     print('-' * 10)
            #     print(method_ref.descriptor)
            #     if method_ref.descriptor in ['(Ljava/lang/String;)V']:
            #         print(StringFactory.object_2_string(frame.stack.pop()))
            #     else:
            #         print(frame.stack.pop())
            #     print(frame.stack.pop())
            #     return
            raise InstructionException('ref {0}.{1} None'.format(method.clazz.name, method.name))

        if method.is_protected and method.clazz.is_superclass(current_class) and \
            method.clazz.package_name != current_class.package_name and \
            ref.clazz != current_class and not ref.clazz.is_subclazz(current_class):
            raise InstructionException('class {0} not vist method {1}.{2} access'.format(current_class.name, method.clazz.name, method.name))

        method = MethodRef.lookup(ref.clazz, method_ref.name, method_ref.descriptor)


        if method is None or method.is_abstract:
            raise InstructionException('method {0}.{1} is abstract'.format(method.clazz.name, method.name))

        self.invoke_method(frame, method)