#encoding: utf-8

from .. import register
from .base import LOAD, LOAD_0, LOAD_1, LOAD_2, LOAD_3


@register(opcode=0X19)
class ALOAD(LOAD):
    pass


@register(opcode=0X2A)
class ALOAD_0(LOAD_0):
    pass


@register(opcode=0X2B)
class ALOAD_1(LOAD_1):
    pass


@register(opcode=0X2C)
class ALOAD_2(LOAD_2):
    pass


@register(opcode=0X2D)
class ALOAD_3(LOAD_3):
    pass
