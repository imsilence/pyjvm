#encoding: utf-8

from abc import ABC

from attribute_info import AttributeFactory

class MemberFactory(object):

    @classmethod
    def parse(cls, clazz, reader, constant_pool):
        count = int(reader.read_16_byte())
        members = []
        for _ in range(count):
            members.append(clazz.parse(reader, constant_pool))

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

    @classmethod
    def parse(cls, reader, constant_pool):
        member = cls(constant_pool)
        member.__constant_pool = constant_pool
        member.__access_flags = member.parse_access_flags(reader)
        member.__name_index = member.parse_name_index(reader)
        member.__descriptor_index = member.parse_decroptor_index(reader)
        member.__attrs = AttributeFactory.parse(reader, constant_pool)
        return member

    def parse_access_flags(self, reader):
        return int(reader.read_16_byte())

    def parse_name_index(self, reader):
        return int(reader.read_16_byte())

    def parse_decroptor_index(self, reader):
        return int(reader.read_16_byte())

    def __repr__(self):
        return self.name



class FieldInfo(Member):
    pass


class MethodInfo(Member):
    pass
