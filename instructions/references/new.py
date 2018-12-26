#encoding: utf-8

from .. import register
from ..base import Index16Instruction
from ..exceptions import InstructionException
from . init import Init


@register(opcode=0XBB)
class NEW(Init, Index16Instruction):

    def execute(self, frame):
        constant_pool = frame.method.clazz.constant_pool

        clazz_ref = constant_pool[self.index]
        clazz = clazz_ref.clazz
        if not clazz.inited:
            frame.revert_next_pc()
            self.init_clazz(frame.thread, clazz)
            return

        if clazz.is_interface or clazz.is_abstract:
            raise InstructionException('class {0} is not instance'.format(clazz.name))

        frame.stack.push(clazz.create_object())