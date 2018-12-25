#encoding: utf-8

from .. import register
from ..base import Index16Instruction
from ..exceptions import InstructionException

@register(opcode=0XB2)
class GET_STATIC(Index16Instruction):

    def execute(self, frame):
        field = frame.method.clazz.constant_pool[self.index].field
        clazz = field.clazz
        if not field.is_static:
            raise InstructionException('field {0}.{1} is not static'.format(clazz.name, field.name))

        frame.stack.push(clazz.static_vars[field.index])
