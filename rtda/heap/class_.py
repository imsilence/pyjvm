#encoding: utf-8

from .access_flags import AccessMixin, AccessFlags
from .class_member import ClassField, ClassMethod
from ..vars_ import Vars
from .constant_pool import ConstantPool
from .object_ import Object
from .array_class import ArrayClassMixin, ArrayTypeFlag

class Class(AccessMixin, ArrayClassMixin):

    def __init__(self):
        self.__access_flags = 0
        self.__name = ''
        self.__super_class_name = ''
        self.__interface_names = []
        self.__constant_pool = None
        self.__fields = []
        self.__methods = []
        self.__loader = None
        self.__super_class = None
        self.__interfaces = []
        self.__instance_var_count = 0
        self.__static_var_count = 0
        self.__static_vars = None
        self.__inited = False
        self.__base_class = None
        self.__source_file = 'unknow'


    def init_class_file(self, class_file):
        self.__access_flags = int(class_file.access_flags)
        self.__name = class_file.class_name
        self.__super_class_name = class_file.super_class_name
        self.__interface_names = class_file.interface_names
        self.__constant_pool = ConstantPool(self, class_file.constant_pool)
        self.__fields = [ClassField(self, field) for field in class_file.fields]
        self.__methods = [ClassMethod(self, method) for method in class_file.methods]
        self.__source_file = class_file.source_file_attr.val if class_file.source_file_attr else 'unknow'


    def init_class_primitive(self, name, loader):
        self.loader = loader
        self.access_flags = AccessFlags.PUBLIC.value
        self.name = name
        self.inited = True


    @property
    def is_primitive(self):
        return ArrayTypeFlag.element(self.name) is not None


    @property
    def access_flags(self):
        return self.__access_flags


    @access_flags.setter
    def access_flags(self, access_flags):
        self.__access_flags = access_flags


    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def java_name(self):
        return self.__name.replace('/', '.')


    @property
    def super_class_name(self):
        return self.__super_class_name


    @super_class_name.setter
    def super_class_name(self, super_class_name):
        self.__super_class_name = super_class_name


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


    @interface_names.setter
    def interface_names(self, interface_names):
        self.__interface_names = interface_names


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


    def get_field(self, name, descriptor, is_static):
        clazz = self
        while clazz:
            for field in clazz.__fields:
                if field.is_static == is_static and \
                    field.name == name and \
                    field.descriptor == descriptor:
                    return field
            clazz = clazz.super_class

        return None


    @property
    def methods(self):
        return self.__methods


    @property
    def static_vars(self):
        return self.__static_vars


    @property
    def package_name(self):
        return self.name.rpartition('/')[0]


    @property
    def inited(self):
        return self.__inited


    @inited.setter
    def inited(self, value=True):
        self.__inited = value


    @property
    def base_class(self):
        return self.__base_class


    @base_class.setter
    def base_class(self, base_class):
        self.__base_class = base_class


    @property
    def source_file(self):
        return self.__source_file



    def alloc_static_vars(self):
        self.__static_vars = Vars(self.static_var_count)


    def is_accessible(self, clazz):
        return self.is_public or clazz.package_name == self.package_name


    def is_subclass(self, clazz):
        super_class = self.super_class
        while super_class:
            if clazz == super_class:
                return True
            super_class = super_class.super_class
        return False


    def is_superclass(self, clazz):
        return clazz.is_subclass(self)


    def create_object(self):
        return Object(self, Vars(self.instance_var_count))


    def is_assignable(self, clazz):
        if self == clazz:
            return True

        if clazz.is_array:
            if self.is_array:
                self.component_class.is_assignable(clazz.component_class)
            else:
                if self.is_interface:
                    pass
                else:
                    pass
        else:
            if clazz.is_interface:
                if self.is_interface:
                    return clazz.is_implements(self)
                else:
                    return clazz.is_subclass(self)
            else:
                if self.is_interface:
                    pass
                else:
                    pass



    def is_subinterface(self, interface):
        for _interface in self.interfaces:
            if _interface == interface or _interface.is_subinterface(interface):
                return True
        return False


    def is_implements(self, interface):
        clazz = self
        while clazz:
            for _interface in clazz.interfaces:
                if _interface == interface or _interface.is_subinterface(interface):
                    return True
            clazz = clazz.super_class

        return False


    def get_main_method(self):
        return self.get_static_method('main', '([Ljava/lang/String;)V')


    def get_clinit_method(self):
        return self.get_static_method('<clinit>', '()V')


    def get_static_method(self, name, descriptor):
        for method in self.__methods:
            if method.is_static and name == method.name and descriptor == method.descriptor:
                return method

        return None


    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, vars(self))

