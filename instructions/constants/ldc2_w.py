#encoding: utf-8

from .. import register
from ..base import Index16Instruction
from .ldc import LDC

@register(opcode=0X14)
class WLDC2(Index16Instruction, LDC):
    pass