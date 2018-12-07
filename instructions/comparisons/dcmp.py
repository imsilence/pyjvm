#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction

class DCMP(NoOperandsInstruction):

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


@register(opcode=0X97)
class DCMPL(DCMP):

    def __init__(self):
        super(DCMPL).__init__()
        self.value = -1


@register(opcode=0X98)
class DCMPG(DCMP):

    def __init__(self):
        super(DCMPG).__init__()
        self.value = 1


