#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction

class FCMP(NoOperandsInstruction):

    def __init__(self):
        self.__value = value


    @property
    def value(self):
        return self.__value


    @value.setter
    def value(self, value):
        self.__value = value


    def execute(self, frame):
        right = frame.stack.pop()
        left = frame.stack.pop()
        value = self.value

        if left is None or right is None:
            pass
        elif left > right:
            value = 1
        elif left == right:
            value = 0
        else:
            value = -1

        frame.stack.push(value)


@register(opcode=0X95)
class FCMPL(FCMP):

    def __init__(self):
        super(FCMPL).__init__()
        self.value = -1


@register(opcode=0X96)
class FCMPG(FCMP):

    def __init__(self):
        super(FCMPG).__init__()
        self.value = 1


