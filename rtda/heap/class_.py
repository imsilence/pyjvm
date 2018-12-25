#encoding: utf-8

from .access_flags import AccessMixin
from .class_member import ClassField, ClassMethod
from ..vars_ import Vars
from .constant_pool import ConstantPool
from .object_ import Object

class Class(AccessMixin):

    def __init__(self, class_file):
        self.__access_flags = int(class_file.access_flags)
        self.__name = class_file.class_name
        self.__super_class_name = class_file.super_class_name
        self.__interface_names = class_file.interface_names
        self.__constant_pool = ConstantPool(self, class_file.constant_pool)
        self.__fields = [ClassField(self, field) for field in class_file.fields]
        self.__methods = [ClassMethod(self, method) for method in class_file.methods]
        self.__loader = None
        self.__super_class = None
        self.__interfaces = []
        self.__instance_var_count = 0
        self.__static_var_count = 0
        self.__static_vars = None


    @property
    def access_flags(self):
        return self.__access_flags


    @property
    def name(self):
        return self.__name


    @property
    def super_class_name(self):
        return self.__super_class_name


    @property
    def constant_pool(self):
        return self.__constant_pool


    @property
    def loader(self):
        return self.__loader


    @loader.setter
    def loader(self, loader):
        self.__loader = loader


    @property
    def super_class(self):
        return self.__super_class


    @super_class.setter
    def super_class(self, super_class):
        self.__super_class = super_class


    @property
    def interface_names(self):
        return self.__interface_names


    @property
    def interfaces(self):
        return self.__interfaces


    @interfaces.setter
    def interfaces(self, interfaces):
        self.__interfaces = interfaces


    @property
    def instance_var_count(self):
        return self.__instance_var_count


    @instance_var_count.setter
    def instance_var_count(self, instance_var_count):
        self.__instance_var_count = instance_var_count


    @property
    def static_var_count(self):
        return self.__static_var_count


    @static_var_count.setter
    def static_var_count(self, static_var_count):
        self.__static_var_count = static_var_count


    @property
    def fields(self):
        return self.__fields


    @property
    def static_vars(self):
        return self.__static_vars


    def alloc_static_vars(self):
        self.__static_vars = Vars(self.static_var_count)


    def is_accessible(self, clazz):
        return self.is_public or clazz.package_name == self.package_name


    @property
    def package_name(self):
        return self.name.rpartition('/')[0]


    def is_subclass(self, clazz):
        super_class = self.super_class
        while super_class:
            if clazz == super_class:
                return True
            super_class = super_class.super_class
        return False


    def create_object(self):
        return Object(self, self.instance_var_count)


    def is_assignable(self, clazz):
        if self == clazz:
            return True

        if self.is_interface:
            clazz.is_subclass(self)
        else:
            clazz.is_implement(self)


    def is_subinterface(self, interface):
        for _interface in self.interfaces:
            if _interface == interface or _interface.is_subinterface(interface):
                return True
        return False


    def is_implement(self, interface):
        clazz = self
        while clazz:
            for _interface in clazz.interfaces:
                if _interface == interface or _interface.is_subinterface(interface):
                    return True
            clazz = clazz.super_class

        return False


    def get_main_method(self):
        return self.get_static_method('main', '([Ljava/lang/String;)V')


    def get_static_method(self, name, descriptor):
        for method in self.__methods:
            if method.is_static and name == method.name and descriptor == method.descriptor:
                return method

        return None