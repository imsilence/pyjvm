#encoding: utf-8

import logging
from abc import ABC, abstractmethod

from exception_info import ExceptionFactory

logger = logging.getLogger(__name__)

class AttributeFactory(object):

    @classmethod
    def parse(cls, reader, constant_pool):
        attrs = []
        count = int(reader.read_16_byte())
        for _ in range(count):
            attr_name_index = int(reader.read_16_byte())
            attr_name = constant_pool[attr_name_index].val
            attr_length = int(reader.read_32_byte())
            clazz = globals().get('Attribute{0}Info'.format(attr_name), AttributeUnparsedInfo)

            if clazz is None:
                logger.critical("not found ConstantInfo for {0}".format(tag.name))
            else:
                instance = clazz(attr_length, constant_pool)
                instance.parse(reader)
                attrs.append(instance)

        return attrs


class AttributeInfo(ABC):

    def __init__(self, length, constant_pool):
        self.__length = length
        self.__constant_pool = constant_pool
        self.__val = None

    def __len__(self):
        return self.__length

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
    def parse(cls, reader):
        return None



class AttributeCodeInfo(AttributeInfo):
    def __init__(self, length, constant_pool):
        super(AttributeCodeInfo, self).__init__(length, constant_pool)
        self.__max_stack = 0
        self.__max_locals = 0
        self.__code = None
        self.__exceptions = []
        self.__attrs = []

    def parse(self, reader):
        self.__max_stack = int(reader.read_16_byte())
        self.__max_locals = int(reader.read_16_byte())

        length = int(reader.read_32_byte())
        self.__code = reader.read_byte(length)
        self.__exceptions = ExceptionFactory.parse(reader)
        self.__attrs = AttributeFactory.parse(reader, self.constant_pool)

    @property
    def val(self):
        return self.__max_stack, self.__max_locals, self.__code, self.__exceptions, self.__attrs


class AttributeConstantValueInfo(AttributeInfo):
    def parse(self, reader):
        self.val = int(reader.read_16_byte())


class AttributeDeprecatedInfo(AttributeInfo):
    pass


class AttributeExceptionsInfo(AttributeInfo):

    def parse(self, reader):
        self.val = reader.read_16_bytes()


class AttributeSourceFileInfo(AttributeInfo):

    def __init__(self, length, constant_pool):
        super(AttributeSourceFileInfo, self).__init__(length, constant_pool)
        self.__index = 0

    def parse(self, reader):
        self.__index = int(reader.read_16_byte())

    @property
    def val(self):
        return self.constant_pool[self.__index].val


class AttributeSyntheticInfo(AttributeInfo):
    pass


class AttributeUnparsedInfo(AttributeInfo):

    def parse(self, reader):
        self.val = reader.read_byte(len(self))

