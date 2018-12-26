#encoding: utf-8

from enum import Enum
import struct

class ByteSize(Enum):
    U1 = 1
    U2 = 2
    U4 = 4
    U8 = 8


class ClassByte(object):

    def __init__(self, byte, start, end):
        self.__byte = byte
        self.__start = start
        self.__end = end

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

    def int(self):
        fmts = {ByteSize.U1.value : '>b', ByteSize.U2.value : '>h', ByteSize.U4.value : '>i', ByteSize.U8.value : '>q'}
        return struct.unpack(fmts.get(len(self.byte)), self.byte)[0]

    def __float__(self):
        return struct.unpack('>f', self.byte)[0]

    def double(self):
        return struct.unpack('>d', self.byte)[0]

    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, vars(self))

    def __str__(self):
        return self.__byte.decode()


class ClassReader(object):

    def __init__(self, data=b''):
        self.__index = 0
        self.__data = data

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index):
        self.__index = index


    def reset(self, data, index):
        self.__data = data
        self.__index = index

    def read_byte(self, n):
        end = self.__index + n
        val = ClassByte(self.__data[self.__index:end], self.__index, end)
        self.__index = end
        return val

    def skip_padding(self):
        if self.__index % 4 != 0:
            self.read_8_byte()

    def read_8_byte(self):
        return self.read_byte(ByteSize.U1.value)

    def read_16_byte(self):
        return self.read_byte(ByteSize.U2.value)

    def read_32_byte(self):
        return self.read_byte(ByteSize.U4.value)

    def read_64_byte(self):
        return self.read_byte(ByteSize.U8.value)

    def read_bytes(self, count, size=ByteSize.U1.value):
        vals = []
        while count > 0:
            vals.append(self.read_byte(size))
            count -= 1
        return vals

    def read_8_bytes(self, n=None):
        return self.read_bytes(n, ByteSize.U1.value)

    def read_16_bytes(self, n=None):
        n = int(self.read_16_byte()) if n is None else n
        return self.read_bytes(n, ByteSize.U2.value)

    def read_32_bytes(self, n=None):
        return self.read_bytes(n, ByteSize.U3.value)

    def read_64_bytes(self, n=None):
        return self.read_bytes(n, ByteSize.U4.value)

    @property
    def data(self):
        return self.__data[self.__index:]