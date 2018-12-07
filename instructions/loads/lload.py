#encoding: utf-8

from .. import register
from .base import LOAD, LOAD_0, LOAD_1, LOAD_2, LOAD_3


@register(opcode=0X16)
class LLOAD(LOAD):
    pass


@register(opcode=0X1E)
class LLOAD_0(LOAD_0):
    pass


@register(opcode=0X1F)
class LLOAD_1(LOAD_1):
    pass


@register(opcode=0X20)
class LLOAD_2(LOAD_2):
    pass

@register(opcode=0X21)
class LLOAD_3(LOAD_3):
    pass
