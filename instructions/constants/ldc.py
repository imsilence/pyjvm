#encoding: utf-8

from .. import register
from ..base import Index8Instruction
from rtda.heap import StringFactory, ClassRef


@register(opcode=0X12)
class LDC(Index8Instruction):

    def execute(self, frame):
        clazz = frame.method.clazz
        constant_pool = clazz.constant_pool
        value = constant_pool[self.index]
        if isinstance(value, str):
            frame.stack.push(StringFactory.get(clazz.loader, value))
        elif isinstance(value, ClassRef):
            frame.stack.push(value.clazz.base_class)
        else:
            frame.stack.push(value)