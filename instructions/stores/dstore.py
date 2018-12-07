#encoding: utf-8

from .. import register
from .base import STORE, STORE_0, STORE_1, STORE_2, STORE_3


@register(opcode=0X39)
class DSTORE(STORE):
    pass


@register(opcode=0X47)
class DSTORE_0(STORE_0):
    pass


@register(opcode=0X48)
class DSTORE_1(STORE_1):
    pass


@register(opcode=0X49)
class DSTORE_2(STORE_2):
    pass


@register(opcode=0X4A)
class DSTORE_3(STORE_3):
    pass
