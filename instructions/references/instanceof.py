#encoding: utf-8

from .. import register
from ..base import Index16Instruction


@register(opcode=0XC1)
class INSTANCE_OF(Index16Instruction):

    def execute(self, frame):
        object_ = frame.stack.pop()
        if object_ is None:
            frame.stack.push(0)
        else:
            constant_pool = frame.method.clazz.constant_pool
            clazz_ref = constant_pool[self.index]
            if object_.is_instance_of(clazz_ref.clazz):
                frame.stack.push(1)
            else:
                frame.stack.push(0)
