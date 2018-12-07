#encoding: utf-8

from ..base import NoOperandsInstruction, Index8Instruction


class LOAD(Index8Instruction):

    def execute(self, frame):
        frame.stack.push(frame.localvars[self.index])


class LOAD_0(NoOperandsInstruction):

    def execute(self, frame):
        frame.stack.push(frame.localvars[0])


class LOAD_1(NoOperandsInstruction):

    def execute(self, frame):
        frame.stack.push(frame.localvars[1])


class LOAD_2(NoOperandsInstruction):

    def execute(self, frame):
        frame.stack.push(frame.localvars[2])


class LOAD_3(NoOperandsInstruction):

    def execute(self, frame):
        frame.stack.push(frame.localvars[3])
