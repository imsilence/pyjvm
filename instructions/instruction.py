#encoding: utf-8

from .exceptions import InstructionException

class InstructionFactory(object):
    INSTRUCTION_MAP = {}

    @classmethod
    def get_instruction(cls, opcode):
        class_name = cls.INSTRUCTION_MAP.get(opcode)
        if class_name is None:
            raise InstructionException('instruction [{0:#X}] not found'.format(opcode))
        return class_name()


def register(opcode):
    def wrapper(cls):
        InstructionFactory.INSTRUCTION_MAP[opcode] = cls
        return cls
    return wrapper