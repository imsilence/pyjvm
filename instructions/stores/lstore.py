#encoding: utf-8

from .. import register
from .base import STORE, STORE_0, STORE_1, STORE_2, STORE_3


@register(opcode=0X37)
class LSTORE(STORE):
    pass


@register(opcode=0X3F)
class LSTORE_0(STORE_0):
    pass


@register(opcode=0X40)
class LSTORE_1(STORE_1):
    pass


@register(opcode=0X41)
class LSTORE_2(STORE_2):
    pass


@register(opcode=0X42)
class LSTORE_3(STORE_3):
    pass
