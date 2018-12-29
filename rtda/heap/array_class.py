#encoding: utf-8

from enum import Enum

from .access_flags import AccessFlags

from .object_ import Object
from .class_member import MethodSignature
from .exceptions import IllegalArrayException

class ArrayType(Enum):
    BOOLEAN = 4
    CHAR = 5
    FLOAT = 6
    DOUBLE = 7
    BYTE = 8
    SHORT = 9
    INT = 10
    LONG = 11

    @classmethod
    def element(cls, value):
        try:
            if value.isdigit():
                return cls(int(value))
        except ValueError as e:
            pass
        return None


class ArrayTypeFlag(Enum):
    VOID = 'V'
    BOOLEAN = 'Z'
    BYTE = 'B'
    SHORT = 'S'
    INT = 'I'
    LONG = 'J'
    CHAR = 'C'
    FLOAT = 'F'
    DOUBLE = 'D'

    @classmethod
    def element(cls, value):
        try:
            return cls(value)
        except ValueError as e:
            return None


class ArrayClassMixin(object):

    def create_array_object(self, count=0):

        atype = ArrayType.element(self.name[1:])
        array = []

        if atype in [ArrayType.BOOLEAN]:
            array = [False]
        elif atype in [ArrayType.CHAR]:
            array = ['']
        elif atype in [ArrayType.FLOAT, ArrayType.DOUBLE]:
            array = [0.0]
        elif atype in [ArrayType.BYTE, ArrayType.SHORT, ArrayType.INT, ArrayType.LONG]:
            array = [0]
        else:
            array = [None]

        return Object(self, array * count)


    def create_multi_array_object(self, counts, array_class=None):
        array_class = array_class if array_class else self
        count = counts[0]
        array = array_class.create_array_object(count)
        if len(counts) > 1:
            for index in range(len(array.fields)):
                array.fields[index] = self.create_multi_array_object(counts[1:], array_class.component_class)

        return array


    def init_class_array(self, name, loader):
        self.loader = loader
        self.access_flags = AccessFlags.PUBLIC.value
        self.name = name
        self.super_class_name = 'java/lang/Object'
        self.super_class = loader.load(self.super_class_name)
        self.interface_names = [
            'java/lang/Cloneable',
            'java/io/Serializable',
        ]

        self.interfaces = [
            loader.load(name) for name in self.interface_names
        ]
        self.inited = True


    @property
    def is_array(self):
        return self.name.startswith('[')


    @property
    def array_class(self):
        class_name = ''
        if self.name.startswith('['):
            class_name = self.name
        else:
            atype = getattr(ArrayType, self.name.upper(), None)
            if atype:
                class_name = str(atype.value)

        return self.loader.load('[' + class_name)


    @property
    def component_class(self):
        if not self.name.startswith('['):
            raise IllegalArrayException('class not is array: {0}'.format(self.name))

        class_name = None

        descriptor = self.name[1:]
        if descriptor.startswith('['):
            class_name = descriptor
        elif descriptor.startswith('L'):
            class_name = descriptor[1:-1]
        else:
            flag = ArrayTypeFlag.element(descriptor)
            if flag:
                class_name = flag.name.lower()

        if class_name is None:
            raise IllegalArrayException('class name is None')

        clazz = self.loader.load(class_name)
        return clazz