#encoding: utf-8

from .access_flags import AccessFlags
from .class_field import ClassField

class Class(object):
    def __init__(self, class_file):
        self.__access_flags = int(class_file.access_flags)
        self.__name = class_file.class_name
        self.__super_class_name = class_file.__super_class_name
        self.__interface_names = class_file.interface_names
        self.__constant_pool = class_file.constant_pool
        self.__fields = [ClassField(self, field) for field in  class_file.fields]
        self.__method = [ClassField(self, method) for method in  class_file.methods]
        self.__loader =
        self.__super_class =
        self.__interfaces =
        self.__instance =
        self.__static =
        self.__static_vars =

    def is_public(self):
        return 0 != (AccessFlags.is_public & self.__access_flags)