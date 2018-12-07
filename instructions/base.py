#encoding: utf-8

from abc import ABC, abstractmethod


class Instruction(ABC):

    @abstractmethod
    def fetch_operands(self, reader):
        pass

    @abstractmethod
    def execute(self, frame):
        pass

    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, vars(self))


class NoOperandsInstruction(Instruction):

    def fetch_operands(self, reader):
        return None


class BranchInstruction(Instruction):

    def __init__(self):
        self.__offset = 0

    @property
    def offset(self):
        return self.__offset.int()

    def fetch_operands(self, reader):
        self.__offset = reader.read_16_byte()

    @abstractmethod
    def is_branch(self, frame):
        pass

    def execute(self, frame):
        if self.is_branch(frame):
            frame.next_pc = frame.thread.pc + self.offset



class IndexInstruction(Instruction):

    def __init__(self):
        self.__index = 0

    @property
    def index(self):
        return int(self.__index)

    @index.setter
    def index(self, index):
        self.__index = index


class Index8Instruction(IndexInstruction):

    def fetch_operands(self, reader):
        self.index = reader.read_8_byte()


class Index16Instruction(IndexInstruction):

    def fetch_operands(self, reader):
        self.index = reader.read_16_byte()