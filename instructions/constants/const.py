#encoding: utf-8

from .. import register
from ..base import NoOperandsInstruction


class ConstInstruction(NoOperandsInstruction):

    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def execute(self, frame):
        frame.stack.push(self.value)


@register(opcode=0X01)
class ACONST_NULL(ConstInstruction):

    def __init__(self):
        super(ACONST_NULL, self).__init__()
        self.value = None


@register(opcode=0X02)
class ICONST_M1(ConstInstruction):

    def __init__(self):
        super(ICONST_M1, self).__init__()
        self.value = -1


@register(opcode=0X03)
class ICONST_0(ConstInstruction):

    def __init__(self):
        super(ICONST_0, self).__init__()
        self.value = 0


@register(opcode=0X04)
class ICONST_1(ConstInstruction):

    def __init__(self):
        super(ICONST_1, self).__init__()
        self.value = 1


@register(opcode=0X05)
class ICONST_2(ConstInstruction):

    def __init__(self):
        super(ICONST_2, self).__init__()
        self.value = 2


@register(opcode=0X06)
class ICONST_3(ConstInstruction):

    def __init__(self):
        super(ICONST_3, self).__init__()
        self.value = 3


@register(opcode=0X07)
class ICONST_4(ConstInstruction):

    def __init__(self):
        super(ICONST_4, self).__init__()
        self.value = 4


@register(opcode=0X08)
class ICONST_5(ConstInstruction):

    def __init__(self):
        super(ICONST_5, self).__init__()
        self.value = 5


@register(opcode=0X09)
class LCONST_0(ConstInstruction):

    def __init__(self):
        super(LCONST_0, self).__init__()
        self.value = 0


@register(opcode=0X0A)
class LCONST_1(ConstInstruction):

    def __init__(self):
        super(LCONST_1, self).__init__()
        self.value = 1


@register(opcode=0X0B)
class FCONST_0(ConstInstruction):

    def __init__(self):
        super(FCONST_0, self).__init__()
        self.value = 0.0


@register(opcode=0X0C)
class FCONST_1(ConstInstruction):

    def __init__(self):
        super(FCONST_1, self).__init__()
        self.value = 1.0


@register(opcode=0X0D)
class FCONST_2(ConstInstruction):

    def __init__(self):
        super(FCONST_2, self).__init__()
        self.value = 2.0


@register(opcode=0X0E)
class DCONST_0(ConstInstruction):

    def __init__(self):
        super(DCONST_0, self).__init__()
        self.value = 0.0


@register(opcode=0X0F)
class DCONST_1(ConstInstruction):

    def __init__(self):
        super(DCONST_1, self).__init__()
        self.value = 1.0


