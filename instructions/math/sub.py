#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction


class SUB(NoOperandsInstruction):

    def execute(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.push(left - right)


@register(opcode=0X64)
class ISUB(SUB):
    pass


@register(opcode=0X65)
class LSUB(SUB):
    pass


@register(opcode=0X66)
class FSUB(SUB):
    pass


@register(opcode=0X67)
class DSUB(SUB):
    pass
