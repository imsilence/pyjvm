#encoding: utf-8

from abc import ABC

from .attribute_info import AttributeFactory, AttributeCodeInfo, AttributeConstantValueInfo

class MemberFactory(object):

    @classmethod
    def parse(cls, clazz, reader, constant_pool):
        count = int(reader.read_16_byte())
        members = []
        for _ in range(count):
            member = clazz(constant_pool)
            member.read(reader)
            members.append(member)
        return members


class Member(ABC):

    def __init__(self, constant_pool):
        self.__constant_pool = constant_pool
        self.__access_flags = 0
        self.__name_index = 0
        self.__descriptor_index = 0
        self.__attrs = []


    @property
    def access_flags(self):
        return self.__access_flags


    @property
    def name(self):
        return self.__constant_pool[self.__name_index].val


    @property
    def descriptor(self):
        return self.__constant_pool[self.__descriptor_index].val


    @property
    def attrs(self):
        return self.__attrs


    def read(self, reader):
        self.__access_flags = reader.read_16_byte()
        self.__name_index = reader.read_16_byte()
        self.__descriptor_index = reader.read_16_byte()
        self.__attrs = AttributeFactory.parse(reader, self.__constant_pool)


    @property
    def code_attr(self):
        for attr in self.attrs:
            if isinstance(attr, AttributeCodeInfo):
                return attr
        return None


    @property
    def constant_value_attr(self):
        for attr in self.attrs:
            if isinstance(attr, AttributeConstantValueInfo):
                return attr
        return None


    def __repr__(self):
        return '{0!r} {1!r} {2!r}'.format(self.name, int(self.access_flags), self.descriptor)



class FieldInfo(Member):
    pass


class MethodInfo(Member):
    pass
