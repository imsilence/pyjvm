#encoding: utf-8

from .. import register
from ..base import Index16Instruction
from ..exceptions import InstructionException

@register(opcode=0XC0)
class CHECK_CAST(Index16Instruction):

    def execute(self, frame):
        object_ = frame.stack.top()
        if object_:
            constant_pool = frame.method.clazz.constant_pool
            clazz_ref = constant_pool[self.index]
            if not object_.is_instance_of(clazz_ref.clazz):
                raise InstructionException('object {0} is not class {1} instance'.format(object_.clazz.name, clazz_ref.clazz.name))
