#encoding: utf-8

from .. import register
from ..base import Index16Instruction
from ..exceptions import InstructionException

@register(opcode=0XB3)
class PUT_STATIC(Index16Instruction):

    def execute(self, frame):
        current_method = frame.method
        current_clazz = current_method.clazz
        field_ref = current_clazz.constant_pool[self.index]
        field = field_ref.field
        clazz = field.clazz
        if not field.is_static:
            raise InstructionException('field {0}.{1} is not static'.format(clazz.name, field.name))

        if field.is_final:
            if current_clazz != clazz or current_method.name != '<clinit>':
                raise InstructionException('field {0}.{1} is final'.format(clazz.name, field.name))

        clazz.static_vars[field.index] = frame.stack.pop()
