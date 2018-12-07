#encoding: utf-8

from ..base import NoOperandsInstruction, Index8Instruction


class STORE(Index8Instruction):

    def execute(self, frame):
        frame.localvars[self.index] = frame.stack.pop()


class STORE_0(NoOperandsInstruction):

    def execute(self, frame):
        frame.localvars[0] = frame.stack.pop()


class STORE_1(NoOperandsInstruction):

    def execute(self, frame):
        frame.localvars[1] = frame.stack.pop()


class STORE_2(NoOperandsInstruction):

    def execute(self, frame):
        frame.localvars[2] = frame.stack.pop()


class STORE_3(NoOperandsInstruction):

    def execute(self, frame):
        frame.localvars[3] = frame.stack.pop()
