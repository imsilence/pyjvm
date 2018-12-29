#encoding: utf-8

from .. import register
from ..base import IndexInstruction
from ..exceptions import InstructionException
from .invoke import InvokeMixin
from rtda.heap import MethodRef


@register(opcode=0XB9)
class INVOKE_INTERFACE(InvokeMixin, IndexInstruction):

    def __init__(self):
        super(INVOKE_INTERFACE, self).__init__()
        self.__count = 0
        self.__zero = 0


    def fetch_operands(self, reader):
        self.index = reader.read_16_byte()
        self.__count = reader.read_8_byte()
        self.__zero = reader.read_8_byte()


    def execute(self, frame):
        current_class = frame.method.clazz
        method_ref = current_class.constant_pool[self.index]
        clazz = method_ref.clazz
        method = method_ref.method

        if method.is_static:
            raise InstructionException('method {0}.{1} is static'.format(method.clazz.name, method.name))

        if method.is_private:
            raise InstructionException('method {0}.{1} is private'.format(method.clazz.name, method.name))

        ref = frame.stack.top(method.signature.var_count)
        if ref is None:
            raise InstructionException('ref {0}.{1} None'.format(method.clazz.name, method.name))

        if not ref.clazz.is_implements(clazz):
            raise InstructionException('class {0} not vist method {1}.{2} access'.format(current_class.name, method.clazz.name, method.name))

        method = MethodRef.lookup(ref.clazz, method_ref.name, method_ref.descriptor)

        if method is None or method.is_abstract:
            raise InstructionException('method {0}.{1} is abstract'.format(method.clazz.name, method.name))

        if not method.is_public:
            raise InstructionException('method {0}.{1} is not public'.format(method.clazz.name, method.name))


        self.invoke_method(frame, method)