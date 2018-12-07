#encoding: utf-8

from .. import register
from .base import STORE, STORE_0, STORE_1, STORE_2, STORE_3


@register(opcode=0X38)
class FSTORE(STORE):
    pass


@register(opcode=0X43)
class FSTORE_0(STORE_0):
    pass


@register(opcode=0X44)
class FSTORE_1(STORE_1):
    pass


@register(opcode=0X45)
class FSTORE_2(STORE_2):
    pass


@register(opcode=0X46)
class FSTORE_3(STORE_3):
    pass
