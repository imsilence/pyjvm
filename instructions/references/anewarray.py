#encoding: utf-8

from .. import register
from ..base import Index16Instruction
from ..exceptions import InstructionException


@register(opcode=0XBD)
class A_NEW_ARRAY(Index16Instruction):

    def execute(self, frame):
        constant_pool = frame.method.clazz.constant_pool
        clazz = constant_pool[self.index].clazz

        count = frame.stack.pop()

        if count < 0:
            raise InstructionException("array size is negative")

        frame.stack.push(clazz.array_class.create_array_object(count))