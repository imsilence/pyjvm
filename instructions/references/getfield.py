#encoding: utf-8

from .. import register
from ..base import Index16Instruction
from ..exceptions import InstructionException

@register(opcode=0XB4)
class GET_FIELD(Index16Instruction):

    def execute(self, frame):
        field = frame.method.clazz.constant_pool[self.index].field
        clazz = field.clazz
        if field.is_static:
            raise InstructionException('field {0}.{1} is static'.format(clazz.name, field.name))

        object_ = frame.stack.pop()

        if object_ is None:
            raise InstructionException('object is None'.format(clazz.name))

        frame.stack.push(object_.fields[field.index])