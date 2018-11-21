#encoding: utf-8

from enum import Enum
import struct

class ByteSize(Enum):
    U1 = 1
    U2 = 2
    U4 = 4
    U8 = 8


class ClassByte(object):

    def __init__(self, byte, start, length):
        self.__byte = byte
        self.__start = start
        self.__end = start + length

    @property
    def byte(self):
        return self.__byte

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    def __int__(self):
        return int.from_bytes(self.byte, byteorder="big")

    def sgint(self):
        fmts = {1 : '>b', 2 : '>h', 4 : '>i', 8 : '>q'}
        return struct.unpack(fmts.get(len(self.byte)), self.byte)[0]

    def __float__(self):
        return struct.unpack('>f', self.byte)[0]

    def __repr__(self):
        return '<{0}>{1}'.format(self.__class__.__name__, vars(self))

    def __str__(self):
        return self.__byte.decode()



class ClassReader(object):

    def __init__(self, data):
        self.__index = 0
        self.__data = data

    def read_byte(self, n):
        val = ClassByte(self.__data[:n], self.__index, n)
        self.__data = self.__data[n:]
        self.__index += n
        return val

    def read_8_byte(self):
        return self.read_byte(ByteSize.U1.value)

    def read_16_byte(self):
        return self.read_byte(ByteSize.U2.value)

    def read_32_byte(self):
        return self.read_byte(ByteSize.U4.value)

    def read_64_byte(self):
        return self.read_byte(ByteSize.U8.value)

    def read_16_bytes(self):
        n = int(self.read_16_byte())
        vals = []
        while n > 0:
            vals.append(self.read_16_byte())
            n -= 1
        return vals