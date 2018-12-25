#encoding: utf-8

from ..base import NoOperandsInstruction, Index8Instruction


class STORE(Index8Instruction):

    def execute(self, frame):
        frame.vars[self.index] = frame.stack.pop()


class STORE_0(NoOperandsInstruction):

    def execute(self, frame):
        frame.vars[0] = frame.stack.pop()


class STORE_1(NoOperandsInstruction):

    def execute(self, frame):
        frame.vars[1] = frame.stack.pop()


class STORE_2(NoOperandsInstruction):

    def execute(self, frame):
        frame.vars[2] = frame.stack.pop()


class STORE_3(NoOperandsInstruction):

    def execute(self, frame):
        frame.vars[3] = frame.stack.pop()
