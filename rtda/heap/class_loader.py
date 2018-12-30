#encoding: utf-8

from classfile import ClassFile
from .class_ import Class
from .array_class import ArrayTypeFlag
from .string import StringFactory

class ClassLoader(object):

    def __init__(self, class_path):
        self.__class_path = class_path
        self.__clazzes = {}
        self.__init_base_class()
        self.__init_primitive_class()


    @property
    def clazzes(self):
        return self.__clazzes



    def __init_base_class(self):
        base_class = self.load("java/lang/Class")
        for name, clazz in self.__clazzes.items():
            if clazz.base_class:
                continue
            clazz.base_class = base_class.create_object()
            clazz.base_class.extra = clazz


    def __init_primitive_class(self):
        for class_name in ArrayTypeFlag.__members__:
            class_name = class_name.lower()
            clazz = Class()
            clazz.init_class_primitive(class_name, self)
            clazz.base_class = self.__clazzes.get("java/lang/Class").create_object()
            clazz.base_class.extra = clazz
            self.__clazzes[class_name] = clazz


    def load(self, class_name):
        clazz = self.__clazzes.get(class_name)
        if clazz is None:
            if class_name.startswith('['):
                clazz = self.__load_array_class(class_name)
            else:
                clazz = self.__load_normal_class(class_name)

            base_class = self.__clazzes.get("java/lang/Class")
            if base_class:
                clazz.base_class = base_class.create_object()
                clazz.base_class.extra = clazz
            self.__clazzes[class_name] = clazz

        return clazz


    def __load_array_class(self, class_name):
        clazz = Class()
        clazz.init_class_array(class_name, self)
        return clazz


    def __load_normal_class(self, class_name):
        clazz = self.__load_class(class_name)
        self.__verify(clazz)
        self.__prepare(clazz)
        return clazz


    def __load_class(self, class_name):
        class_bytes = self.__class_path.read_class(class_name)
        class_file = ClassFile.parse(class_bytes)

        clazz = Class()
        clazz.init_class_file(class_file)
        clazz.loader = self
        if clazz.name != 'java/lang/Object':
            clazz.super_class = self.load(clazz.super_class_name)

        interfaces = []
        for interface_name in clazz.interface_names:
            interfaces.append(self.load(interface_name))

        clazz.interfaces = interfaces
        return clazz


    def __verify(self, clazz):
        pass


    def __prepare(self, clazz):
        self.__prepare_instance_var_count(clazz)
        self.__prepare_static_var_count(clazz)
        self.__prepare_static_vars(clazz)


    def __prepare_instance_var_count(self, clazz):
        index = 0
        if clazz.super_class:
            index += clazz.super_class.instance_var_count

        for field in clazz.fields:
            if field.is_static:
                continue
            field.index = index
            index += 1

        clazz.instance_var_count = index


    def __prepare_static_var_count(self, clazz):
        index = 0
        for field in clazz.fields:
            if not field.is_static:
                continue

            field.index = index
            index += 1

        clazz.static_var_count = index


    def __prepare_static_vars(self, clazz):
        clazz.alloc_static_vars()
        constant_pool = clazz.constant_pool

        for field in clazz.fields:
            if field.is_static and field.is_final and field.const_value_index > 0:
                value = constant_pool[field.const_value_index]
                if field.descriptor in ['Ljava/lang/String']:
                    value = StringFactory.get(clazz.loader, value)
                clazz.static_vars[field.index] = value
