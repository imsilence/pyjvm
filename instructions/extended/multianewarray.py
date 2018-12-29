#encoding: utf-8

from .. import register
from ..base import Instruction
from ..exceptions import InstructionException


@register(opcode=0XC5)
class MULTI_A_NEW_ARRAY(Instruction):

    def __init__(self):
        self.__index = 0
        self.__dimensions = 0

    def fetch_operands(self, reader):
        self.__index = int(reader.read_16_byte())
        self.__dimensions = int(reader.read_8_byte())


    def execute(self, frame):
        constant_pool = frame.method.clazz.constant_pool
        clazz = constant_pool[self.__index].clazz

        counts = [0] * self.__dimensions

        for index in range(self.__dimensions - 1, -1, -1):
            count = frame.stack.pop()
            if count < 0:
                raise InstructionException("array size is negative")
            counts[index] = count


        frame.stack.push(clazz.create_multi_array_object(counts))