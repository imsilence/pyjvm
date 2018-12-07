#encoding: utf-8

from .. import register
from .base import STORE, STORE_0, STORE_1, STORE_2, STORE_3

@register(opcode=0X36)
class ISTORE(STORE):
    pass


@register(opcode=0X3B)
class ISTORE_0(STORE_0):
    pass


@register(opcode=0X3C)
class ISTORE_1(STORE_1):
    pass


@register(opcode=0X3D)
class ISTORE_2(STORE_2):
    pass


@register(opcode=0X3E)
class ISTORE_3(STORE_3):
    pass
