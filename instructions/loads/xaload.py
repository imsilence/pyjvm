#encoding: utf-8

from .. import register
from .base import XALOAD


@register(opcode=0X2E)
class IALOAD(XALOAD):
    pass


@register(opcode=0X2F)
class LALOAD(XALOAD):
    pass


@register(opcode=0X30)
class FALOAD(XALOAD):
    pass



@register(opcode=0X31)
class DALOAD(XALOAD):
    pass


@register(opcode=0X32)
class AALOAD(XALOAD):
    pass


@register(opcode=0X33)
class BALOAD(XALOAD):
    pass


@register(opcode=0X34)
class CALOAD(XALOAD):
    pass


@register(opcode=0X35)
class SALOAD(XALOAD):
    pass
