#encoding: utf-8

from .. import register
from ..base import Index16Instruction
from ..exceptions import InstructionException

@register(opcode=0XB5)
class PUT_FIELD(Index16Instruction):

    def execute(self, frame):
        current_method = frame.method
        current_clazz = current_method.clazz
        field_ref = current_clazz.constant_pool[self.index]
        field = field_ref.field
        clazz = field.clazz
        if field.is_static:
            raise InstructionException('field {0}.{1} is static'.format(clazz.name, field.name))

        if field.is_final:
            if current_clazz != clazz or current_method.name != '<init>':
                raise InstructionException('field {0}.{1} is final'.format(clazz.name, field.name))

        value = frame.stack.pop()

        object_ = frame.stack.pop()

        if object_ is None:
            raise InstructionException('object {0} is None'.format(object_.clazz.name))

        object_.fields[field.index] = value
