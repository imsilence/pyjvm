#encoding: utf-8

from .. import register
from .base import XASTORE


@register(opcode=0X4F)
class IASTORE(XASTORE):
    pass


@register(opcode=0X50)
class LASTORE(XASTORE):
    pass


@register(opcode=0X51)
class FASTORE(XASTORE):
    pass


@register(opcode=0X52)
class DASTORE(XASTORE):
    pass


@register(opcode=0X53)
class AASTORE(XASTORE):
    pass


@register(opcode=0X54)
class BASTORE(XASTORE):
    pass


@register(opcode=0X55)
class CASTORE(XASTORE):
    pass


@register(opcode=0X56)
class SASTORE(XASTORE):
    pass