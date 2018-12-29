#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction
from ..exceptions import InstructionException


@register(opcode=0XBE)
class ARRAY_LENGTH(NoOperandsInstruction):

    def execute(self, frame):
        array = frame.stack.pop()

        if array is None:
            raise InstructionException('array is None')

        frame.stack.push(len(array))