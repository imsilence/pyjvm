#encoding: utf-8

from .. import register
from ..base import Instruction
from ..exceptions import InstructionException


@register(opcode=0XBC)
class NEW_ARRAY(Instruction):

    def __init__(self):
        self.__atype = 0


    def fetch_operands(self, reader):
        self.__atype = reader.read_8_byte()


    def execute(self, frame):
        count = frame.stack.pop()

        if count < 0:
            raise InstructionException("array size is negative")

        loader = frame.method.clazz.loader
        clazz = loader.load('[{0}'.format(int(self.__atype)))
        frame.stack.push(clazz.create_array_object(count))