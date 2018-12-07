#encoding: utf-8

import logging
from abc import ABC, abstractmethod

from .exception_table_entry import ExceptionTableEntryFactory
from .line_number_table_entry import LineNumberTableEntryFactory

logger = logging.getLogger(__name__)

class AttributeFactory(object):

    @classmethod
    def parse(cls, reader, constant_pool):
        attrs = []
        count = int(reader.read_16_byte())
        for _ in range(count):
            attr_name_index = reader.read_16_byte()
            attr_name = constant_pool[attr_name_index].val

            attr_length = reader.read_32_byte()

            clazz = globals().get('Attribute{0}Info'.format(attr_name), AttributeUnparsedInfo)

            instance = clazz(int(attr_length), constant_pool)
            instance.read(reader)
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
    def read(cls, reader):
        return None

    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, self.val)


class AttributeCodeInfo(AttributeInfo):
    def __init__(self, length, constant_pool):
        super(AttributeCodeInfo, self).__init__(length, constant_pool)
        self.__max_stack = 0
        self.__max_locals = 0
        self.__code = None
        self.__exceptions = []
        self.__attrs = []

    def read(self, reader):
        self.__max_stack = reader.read_16_byte()
        self.__max_locals = reader.read_16_byte()

        length = reader.read_32_byte()
        self.__code = reader.read_byte(int(length))
        self.__exceptions = ExceptionTableEntryFactory.parse(reader)
        self.__attrs = AttributeFactory.parse(reader, self.constant_pool)

    @property
    def max_stack(self):
        return int(self.__max_stack)

    @property
    def max_locals(self):
        return int(self.__max_locals)

    @property
    def code(self):
        return self.__code

    @property
    def val(self):
        return int(self.__max_stack), int(self.__max_locals), self.__code, self.__exceptions, self.__attrs


class AttributeConstantValueInfo(AttributeInfo):
    def __init__(self, length, constant_pool):
        super(AttributeConstantValueInfo, self).__init__(length, constant_pool)
        self.__constant_value_index = 0

    def read(self, reader):
        self.__constant_value_index = reader.read_16_byte()

    @property
    def val(self):
        return self.constant_pool[self.__constant_value_index].val


class AttributeDeprecatedInfo(AttributeInfo):

    def read(self, reader):
        self.val = None


class AttributeExceptionsInfo(AttributeInfo):

    def read(self, reader):
        self.val = reader.read_16_bytes()


class AttributeSourceFileInfo(AttributeInfo):

    def __init__(self, length, constant_pool):
        super(AttributeSourceFileInfo, self).__init__(length, constant_pool)
        self.__source_file_index = 0

    def read(self, reader):
        self.__source_file_index = reader.read_16_byte()

    @property
    def val(self):
        return self.constant_pool[self.__source_file_index].val


class AttributeSyntheticInfo(AttributeInfo):
    def read(self, reader):
        self.val = None


class AttributeUnparsedInfo(AttributeInfo):

    def read(self, reader):
        self.val = reader.read_byte(len(self))


class AttributeLineNumberTableInfo(AttributeInfo):

    def __init__(self, length, constant_pool):
        super(AttributeLineNumberTableInfo, self).__init__(length, constant_pool)
        self.__line_numbers = []

    def read(self, reader):
        self.__line_numbers = LineNumberTableEntryFactory.parse(reader)

    @property
    def val(self):
        return self.__line_numbers

