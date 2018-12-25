#encoding: utf-8

from .. import register
from ..base import Index16Instruction
from .ldc import LDC

@register(opcode=0X13)
class WLDC(Index16Instruction, LDC):
    pass