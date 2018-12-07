#encoding: utf-8

from .. import register
from .base import STORE, STORE_0, STORE_1, STORE_2, STORE_3


@register(opcode=0X3A)
class ASTORE(STORE):
    pass


@register(opcode=0X4B)
class ASTORE_0(STORE_0):
    pass


@register(opcode=0X4C)
class ASTORE_1(STORE_1):
    pass


@register(opcode=0X4D)
class ASTORE_2(STORE_2):
    pass


@register(opcode=0X4E)
class ASTORE_3(STORE_3):
    pass
