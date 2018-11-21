#encoding: utf-8

import logging
from enum import Enum
from abc import ABC, abstractmethod

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
    def get_constant_info(cls, reader, constant_pool):
        byte = int(reader.read_8_byte())
        tag = ConstantTag(byte)
        clazz = globals().get('Constant{0}Info'.format(tag.name), None)
        instance = None
        if clazz is None:
            logger.critical("not found ConstantInfo for {0}".format(tag.name))
        else:
            instance = clazz(constant_pool)
            instance.parse(reader)
        return instance


class ConstantPool(object):

    def __init__(self):
        self.__infos = []

    @classmethod
    def parse(cls, reader):
        count = int(reader.read_16_byte())
        pool = cls()
        while count > 1:
            info = ConstantInfoFactory.get_constant_info(reader, pool)
            count -= 1
            pool.__infos.append(info)
            if isinstance(info, (ConstantLongInfo, ConstantDoubleInfo)):
                count -= 1
                pool.__infos.append(info)
        return pool

    def __getitem__(self, index):
        # info中的index从1开始, list中从0开始, 需要
        return self.__infos[index - 1]

    def __len__(self):
        return len(self.__infos)

    def class_name(self, index):
        return self[index].val

    def name_type(self, index):
        return self[index].val


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
    def parse(self, reader):
        pass


class ConstantUtf8Info(ConstantInfo):

    def parse(self, reader):
        length = int(reader.read_16_byte())
        self.val = str(reader.read_byte(length))


class ConstantIntegerInfo(ConstantInfo):

    def parse(self, reader):
        #有符号整数
        self.val = reader.read_32_byte().sgint()


class ConstantFloatInfo(ConstantInfo):

    def parse(self, reader):
        self.val = float(reader.read_32_byte())


class ConstantLongInfo(ConstantInfo):

    def parse(self, reader):
        #有符号整数
        self.val = reader.read_64_byte().sgint()


class ConstantDoubleInfo(ConstantInfo):

    def parse(self, reader):
        self.val = float(reader.read_64_byte())


class ConstantClassInfo(ConstantInfo):

    def __init__(self, constant_pool):
        super(ConstantClassInfo, self).__init__(constant_pool)
        self.__index = 0

    def parse(self, reader):
        self.__index = int(reader.read_16_byte())

    @property
    def index(self):
        return self.__index

    @property
    def val(self):
        return self.constant_pool[self.__index].val


class ConstantStringInfo(ConstantInfo):

    def __init__(self, constant_pool):
        super(ConstantStringInfo, self).__init__(constant_pool)
        self.__index = 0

    def parse(self, reader):
        self.__index = int(reader.read_16_byte())

    @property
    def val(self):
        return self.constant_pool[self.__index].val


class ConstantRefInfo(ConstantInfo):

    def __init__(self, constant_pool):
        super(ConstantRefInfo, self).__init__(constant_pool)
        self.__class_index = 0
        self.__name_and_type_index = 0

    def parse(self, reader):
        self.__class_index = int(reader.read_16_byte())
        self.__name_and_type_index = int(reader.read_16_byte())

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


class ConstantNameAndTypeInfo(ConstantInfo):

    def __init__(self, constant_pool):
        super(ConstantNameAndTypeInfo, self).__init__(constant_pool)
        self.__name_index = 0
        self.__descriptor_index = 0

    def parse(self, reader):
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