#encoding: utf-8

from ..math.iinc import IINC

class WIINC(IINC):

    def fetch_operands(self, reader):
        self.__index = int(reader.read_16_byte())
        self.__const = reader.read_16_byte().int()
