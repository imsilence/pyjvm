#encoding: utf-8

from .. import register
from .base import LOAD, LOAD_0, LOAD_1, LOAD_2, LOAD_3


@register(opcode=0X17)
class FLOAD(LOAD):
    pass


@register(opcode=0X22)
class FLOAD_0(LOAD_0):
    pass


@register(opcode=0X23)
class FLOAD_1(LOAD_1):
    pass


@register(opcode=0X24)
class FLOAD_2(LOAD_2):
    pass


@register(opcode=0X25)
class FLOAD_3(LOAD_3):
    pass
