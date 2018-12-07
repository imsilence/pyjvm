#encoding: utf-8

class InstructionException(Exception):
    pass


class InstructionFactory(object):
    INSTRUCTION_MAP = {}

    @classmethod
    def get_instruction(cls, opcode):
        clazz_name = cls.INSTRUCTION_MAP.get(opcode)
        if clazz_name is None:
            raise InstructionException('instruction [{0:#X}] not found'.format(opcode))
        return clazz_name()


def register(opcode):
    def wrapper(cls):
        InstructionFactory.INSTRUCTION_MAP[opcode] = cls
        return cls
    return wrapper