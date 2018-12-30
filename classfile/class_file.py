#encoding: utf-8

import logging

from .exceptions import ClassFormatException
from .constant_info import ConstantPool
from .class_reader import ClassReader
from .member_info import MemberFactory, FieldInfo, MethodInfo
from .attribute_info import AttributeFactory, AttributeSourceFileInfo

logger = logging.getLogger(__name__)


class ClassFile(object):

    def __init__(self):
        self.__class_name = ''
        self.__magic = 0
        self.__minor_version = 0
        self.__major_version = 0
        self.__constant_pool = []
        self.__access_flags = 0
        self.__this_class = 0
        self.__super_class = 0
        self.__interfaces = []
        self.__fields = []
        self.__methods = []
        self.__attrs = []


    @property
    def magic(self):
        return int(self.__magic)


    @property
    def version(self):
        return '{0}.{1}'.format(int(self.__major_version), int(self.__minor_version))


    @property
    def constant_pool(self):
        return self.__constant_pool


    @property
    def access_flags(self):
        return self.__access_flags


    @property
    def fields(self):
        return self.__fields


    @property
    def methods(self):
        return self.__methods


    @property
    def attrs(self):
        return self.__attrs


    @property
    def class_name(self):
        return self.constant_pool[self.__this_class].val


    @property
    def interface_names(self):
        return [self.constant_pool[x].val for x in self.__interfaces]


    @property
    def super_class_name(self):
        return self.constant_pool[self.__super_class].val if int(self.__super_class) > 0 else ""


    @property
    def source_file_attr(self):
        for attr in self.__attrs:
            if isinstance(attr, AttributeSourceFileInfo):
                return attr
        return None


    @classmethod
    def parse(cls, class_bytes):
        reader = ClassReader(class_bytes)

        class_file = cls()
        class_file.read(reader)

        return class_file


    def read(self, reader):
        self.__magic = self.read_magic(reader)
        self.__major_version, self.__minor_version = self.read_version(reader)
        self.__constant_pool = ConstantPool.parse(reader)
        self.__access_flags = reader.read_16_byte()
        self.__this_class = reader.read_16_byte()
        self.__super_class = reader.read_16_byte()
        self.__interfaces = reader.read_16_bytes()

        self.__fields =  MemberFactory.parse(FieldInfo, reader, self.__constant_pool)

        self.__methods =  MemberFactory.parse(MethodInfo, reader, self.__constant_pool)

        self.__attrs = AttributeFactory.parse(reader, self.__constant_pool)


    def read_magic(self, reader):
        magic = reader.read_32_byte()
        if 0XCAFEBABE != int(magic):
            raise ClassFormatException("class file magic error")
        return magic


    def read_version(self, reader):
        minor_version = reader.read_16_byte()
        major_version = reader.read_16_byte()

        if int(major_version) == 45 or int(major_version) in range(46, 53) and int(minor_version) == 0:
            return major_version, minor_version

        raise ClassFormatException("class file version error")


    def __repr__(self):
        return '<{0}!r>{1!r}'.format(self.__class__.__name__, vars(self))