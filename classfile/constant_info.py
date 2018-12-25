#encoding: utf-8

import logging
from enum import Enum
from abc import ABC, abstractmethod

from .exceptions import ConstantInfoNotFoundException

logger = logging.getLogger(__name__)


class ConstantTag(Enum):

    Utf8 = 1
    Integer = 3
    Float = 4
    Long = 5
    Double = 6

    Class = 7

    String = 8

    Fieldref = 9
    Methodref = 10
    InterfaceMethodref = 11

    NameAndType = 12
    MethodHandle = 15
    MethodType = 16
    InvokeDynamic = 18


class ConstantInfoFactory(object):

    @classmethod
    def parse(cls, reader, constant_pool):
        byte = int(reader.read_8_byte())

        tag = ConstantTag(byte)

        class_name = 'Constant{0}Info'.format(tag.name)
        clazz = globals().get(class_name, None)

        if clazz is None:
            logger.critical("not found ConstantInfo for {0}".format(tag.name))
            raise ConstantInfoNotFoundException("class not found[{0}]".format(class_name))
        else:
            instance = clazz(constant_pool)
            instance.read(reader)
            return instance


class ConstantPool(object):

    def __init__(self):
        self.__infos = []


    @property
    def infos(self):
        return self.__infos


    @classmethod
    def parse(cls, reader):
        count = int(reader.read_16_byte())
        pool = cls()
        while count > 1:
            info = ConstantInfoFactory.parse(reader, pool)
            count -= 1
            pool.__infos.append(info)
            if isinstance(info, (ConstantLongInfo, ConstantDoubleInfo)):
                count -= 1
                pool.__infos.append(info)
        return pool

    def __getitem__(self, index):
        # info中的index从1开始, list中从0开始, 需要转换
        # index可能为ClassByte, 做int转换
        return self.__infos[int(index) - 1]

    def __len__(self):
        return len(self.__infos)


class ConstantInfo(ABC):

    def __init__(self, constant_pool):
        self.__constant_pool = constant_pool
        self.__val = None


    @property
    def val(self):
        return self.__val


    @val.setter
    def val(self, value):
        self.__val = value


    @property
    def constant_pool(self):
        return self.__constant_pool


    @abstractmethod
    def read(self, reader):
        pass

    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, self.val)


class ConstantUtf8Info(ConstantInfo):

    def read(self, reader):
        length = int(reader.read_16_byte())
        self.val = str(reader.read_byte(length))


class ConstantIntegerInfo(ConstantInfo):

    def read(self, reader):
        #有符号整数
        self.val = reader.read_32_byte().int()


class ConstantFloatInfo(ConstantInfo):

    def read(self, reader):
        self.val = float(reader.read_32_byte())


class ConstantLongInfo(ConstantInfo):

    def read(self, reader):
        #有符号整数
        self.val = reader.read_64_byte().int()


class ConstantDoubleInfo(ConstantInfo):

    def read(self, reader):
        self.val = reader.read_64_byte().double()


class ConstantClassInfo(ConstantInfo):

    def __init__(self, constant_pool):
        super(ConstantClassInfo, self).__init__(constant_pool)
        self.__name_index = 0


    def read(self, reader):
        self.__name_index = reader.read_16_byte()


    @property
    def val(self):
        return self.constant_pool[self.__name_index].val


class ConstantStringInfo(ConstantInfo):

    def __init__(self, constant_pool):
        super(ConstantStringInfo, self).__init__(constant_pool)
        self.__index = 0


    def read(self, reader):
        self.__index = reader.read_16_byte()


    @property
    def val(self):
        return self.constant_pool[self.__index].val


class ConstantNameAndTypeInfo(ConstantInfo):

    def __init__(self, constant_pool):
        super(ConstantNameAndTypeInfo, self).__init__(constant_pool)
        self.__name_index = 0
        self.__descriptor_index = 0


    def read(self, reader):
        self.__name_index = int(reader.read_16_byte())
        self.__descriptor_index = int(reader.read_16_byte())


    @property
    def name(self):
        return self.constant_pool[self.__name_index].val


    @property
    def descriptor(self):
        return self.constant_pool[self.__descriptor_index].val


    @property
    def val(self):
        return self.name, self.descriptor


class ConstantRefInfo(ConstantInfo):

    def __init__(self, constant_pool):
        super(ConstantRefInfo, self).__init__(constant_pool)
        self.__class_index = 0
        self.__name_and_type_index = 0


    def read(self, reader):
        self.__class_index = reader.read_16_byte()
        self.__name_and_type_index = reader.read_16_byte()


    @property
    def class_name(self):
        return self.constant_pool[self.__class_index].val


    @property
    def name_and_type(self):
        return self.constant_pool[self.__name_and_type_index].val


    @property
    def val(self):
        return self.class_name, self.name_and_type


class ConstantFieldrefInfo(ConstantRefInfo):
    pass


class ConstantMethodrefInfo(ConstantRefInfo):
    pass


class ConstantInterfaceMethodrefInfo(ConstantRefInfo):
    pass

