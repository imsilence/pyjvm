#encoding: utf-8

from .. import register
from ..base import Instruction

from .loads_w import WILOAD, WLLOAD, WFLOAD, WDLOAD, WALOAD
from .stores_w import WISTORE, WLSTORE, WFSTORE, WDSTORE, WASTORE
from .iinc_w import WIINC


@register(opcode=0XC4)
class WIDE(Instruction):

    INSTRUCTION_MAP = {
        0X15: WILOAD, #iload
        0X16: WLLOAD, #lload
        0X17: WFLOAD, #fload
        0X18: WDLOAD, #dload
        0X19: WALOAD, #aload
        0X36: WISTORE, #istore
        0X37: WLSTORE, #lstore
        0X38: WFSTORE, #fstore
        0X39: WDSTORE, #dstore
        0X3a: WASTORE, #astore
        0X84: WIINC, #iinc
        0Xa9: None, #ret
    }

    def __init__(self):
        self.__instruction = None

    def fetch_operands(self, reader):
        opcode = int(reader.read_8_byte())
        self.__instruction = self.INSTRUCTION_MAP.get(int(opcode))
        if self.__instruction:
            self.__instruction.fetch_operands(reader, True)

    def execute(self, frame):
        self.__instruction.execute()