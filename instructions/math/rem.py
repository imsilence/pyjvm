#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction

class REM(NoOperandsInstruction):

    def execute(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.push(left % right)


@register(opcode=0X70)
class IREM(REM):
    pass


@register(opcode=0X71)
class LREM(REM):
    pass


@register(opcode=0X72)
class FREM(REM):
    pass


@register(opcode=0X73)
class DREM(REM):
    pass





