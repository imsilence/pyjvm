#encoding: utf-8

import logging

from constant_info import ConstantPool
from class_reader import ClassReader
from member_info import MemberFactory, FieldInfo, MethodInfo
from attribute_info import AttributeFactory

logger = logging.getLogger(__name__)

class ClassFormatException(Exception):
    pass


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
        return self.__magic

    @property
    def version(self):
        return '{0}.{1}'.format(self.__major_version, self.__minor_version)

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
    def class_name(self):
        return self.constant_pool.class_name(self.__this_class)

    @property
    def interface_names(self):
        return [self.constant_pool[x].val for x in self.__interfaces]

    @property
    def super_class_name(self):
        return self.constant_pool.class_name(self.__super_class) if  self.__super_class > 0 else ""

    @classmethod
    def parse(cls, class_bytes):
        reader = ClassReader(class_bytes)

        class_file = cls()

        class_file.__magic = class_file.parse_magic(reader)
        class_file.__major_version, class_file.__minor_version = class_file.parse_version(reader)
        class_file.__constant_pool = ConstantPool.parse(reader)
        class_file.__access_flags = int(reader.read_16_byte())
        class_file.__this_class = int(reader.read_16_byte())
        class_file.__super_class = int(reader.read_16_byte())
        class_file.__interfaces = [int(x) for x in reader.read_16_bytes()]
        class_file.__fields =  MemberFactory.parse(FieldInfo, reader, class_file.__constant_pool)
        class_file.__methods =  MemberFactory.parse(MethodInfo, reader, class_file.__constant_pool)
        # class_file.__attrs = AttributeFactory.parse(reader, class_file.__constant_pool)
        return class_file


    def parse_magic(self, reader):
        magic = int(reader.read_32_byte())
        if 0XCAFEBABE != magic:
            raise ClassFormatException("class file magic error")
        return magic

    def parse_version(self, reader):
        minor_version = int(reader.read_16_byte())
        major_version = int(reader.read_16_byte())

        if major_version == 45 or major_version in range(46, 53) and minor_version == 0:
            return major_version, minor_version

        raise ClassFormatException("class file version error")

    def __repr__(self):
        return '<{0}>{1}'.format(self.__class__.__name__, vars(self))