#encoding: utf-8

class ClassMember(object):

    def __init__(self, class_, member):
        self.__access_flags = int(member.access_flags)
        self.__name = member.name
        self.__descriptor = member.descriptor
        self.__class = class_