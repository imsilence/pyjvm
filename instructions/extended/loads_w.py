#encoding: utf-8

from ..base import Index16Instruction

from ..loads.iload import ILOAD
from ..loads.lload import LLOAD
from ..loads.fload import FLOAD
from ..loads.dload import DLOAD
from ..loads.aload import ALOAD


class WILOAD(Index16Instruction, ILOAD):
    pass


class WLLOAD(Index16Instruction, LLOAD):
    pass


class WFLOAD(Index16Instruction, FLOAD):
    pass


class WDLOAD(Index16Instruction, DLOAD):
    pass


class WALOAD(Index16Instruction, ALOAD):
    pass
