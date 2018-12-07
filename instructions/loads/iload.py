#encoding: utf-8

from .. import register
from .base import LOAD, LOAD_0, LOAD_1, LOAD_2, LOAD_3


@register(opcode=0X15)
class ILOAD(LOAD):
    pass


@register(opcode=0X1A)
class ILOAD_0(LOAD_0):
    pass


@register(opcode=0X1B)
class ILOAD_1(LOAD_1):
    pass


@register(opcode=0X1C)
class ILOAD_2(LOAD_2):
    pass


@register(opcode=0X1D)
class ILOAD_3(LOAD_3):
    pass
