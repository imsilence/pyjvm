#encoding: utf-8

from ..base import Index16Instruction

from ..stores.istore import ISTORE
from ..stores.lstore import LSTORE
from ..stores.fstore import FSTORE
from ..stores.dstore import DSTORE
from ..stores.astore import ASTORE

class WISTORE(Index16Instruction, ISTORE):
    pass


class WLSTORE(Index16Instruction, LSTORE):
    pass


class WFSTORE(Index16Instruction, FSTORE):
    pass


class WDSTORE(Index16Instruction, DSTORE):
    pass


class WASTORE(Index16Instruction, ASTORE):
    pass