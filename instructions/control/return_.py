#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction


class RETURN(NoOperandsInstruction):
    def execute(self, frame):
        thread = frame.treahd
        current_frame = thread.pop_frame()
        invoker_frame = thread.top_frame()
        invoker_frame.push(current_frame.stack.pop())


@register(opcode=0XAC)
class IRETURN(RETURN):
    pass


@register(opcode=0XAD)
class LRETURN(RETURN):
    pass


@register(opcode=0XAE)
class FRETURN(RETURN):
    pass


@register(opcode=0XAF)
class DETURN(RETURN):
    pass


@register(opcode=0XB0)
class ARETURN(RETURN):
    pass


@register(opcode=0XB1)
class VRETURN(NoOperandsInstruction):

    def execute(self, frame):
        frame.thread.pop_frame()