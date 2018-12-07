#encoding: utf-8

from .. import register
from .base import LOAD, LOAD_0, LOAD_1, LOAD_2, LOAD_3


@register(opcode=0X18)
class DLOAD(LOAD):
    pass


@register(opcode=0X26)
class DLOAD_0(LOAD_0):
    pass


@register(opcode=0X27)
class DLOAD_1(LOAD_1):
    pass


@register(opcode=0X28)
class DLOAD_2(LOAD_2):
    pass


@register(opcode=0X29)
class DLOAD_3(LOAD_3):
    pass