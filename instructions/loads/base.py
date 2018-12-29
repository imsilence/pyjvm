#encoding: utf-8

from ..base import NoOperandsInstruction, Index8Instruction
from ..exceptions import InstructionException

class LOAD(Index8Instruction):

    def execute(self, frame):
        frame.stack.push(frame.vars[self.index])


class LOAD_0(NoOperandsInstruction):

    def execute(self, frame):
        frame.stack.push(frame.vars[0])


class LOAD_1(NoOperandsInstruction):

    def execute(self, frame):
        frame.stack.push(frame.vars[1])


class LOAD_2(NoOperandsInstruction):

    def execute(self, frame):
        frame.stack.push(frame.vars[2])


class LOAD_3(NoOperandsInstruction):

    def execute(self, frame):
        frame.stack.push(frame.vars[3])


class XALOAD(NoOperandsInstruction):

    def execute(self, frame):
        index = frame.stack.pop()
        array = frame.stack.pop()
        if array is None:
            raise InstructionException('array is None')

        if index < 0 or index >= len(array):
            raise InstructionException('array index error')

        frame.stack.push(array[index])