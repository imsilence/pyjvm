#encoding: utf-8

from classfile.constant_info import ConstantUtf8Info, \
                                    ConstantIntegerInfo, ConstantFloatInfo, \
                                    ConstantLongInfo, ConstantDoubleInfo, \
                                    ConstantClassInfo, \
                                    ConstantStringInfo, \
                                    ConstantFieldrefInfo, ConstantMethodrefInfo, \
                                    ConstantInterfaceMethodrefInfo


from .exceptions import IllegalAccessException


class Constant(object):
    pass


class ConstantPool(object):

    def __init__(self, clazz, constant_pool):
        self.__clazz = clazz
        self.__consts = self.__tl(constant_pool)


    def __tl(self, constant_pool):
        consts = []

        for index in range(1, 1 + len(constant_pool)):
            info = constant_pool[index]
            if isinstance(info, (ConstantUtf8Info, ConstantIntegerInfo, ConstantFloatInfo, ConstantStringInfo)):
                consts.append(info.val)
            elif isinstance(info, (ConstantLongInfo, ConstantDoubleInfo)):
                consts.append(info.val)
            elif isinstance(info, ConstantClassInfo):
                consts.append(ClassRef(self, info))
            elif isinstance(info, ConstantFieldrefInfo):
                consts.append(FieldRef(self, info))
            elif isinstance(info, ConstantMethodrefInfo):
                consts.append(MethodRef(self, info))
            elif isinstance(info, ConstantInterfaceMethodrefInfo):
                consts.append(InterfaceMethodRef(self, info))
            else:
                consts.append(None)

        return consts


    def __getitem__(self, index):
        return self.__consts[int(index) - 1]


    @property
    def clazz(self):
        return self.__clazz


    @property
    def consts(self):
        return self.__consts


    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, vars(self))


class SymRef(object):

    def __init__(self, constant_pool, class_name=''):
        self.__constant_pool = constant_pool
        self.__class_name = class_name
        self.__clazz = None


    @property
    def class_name(self):
        return self.__class_name


    @property
    def constant_pool(self):
        return self.__constant_pool


    @property
    def clazz(self):
        if self.__clazz is None:
            pclazz = self.constant_pool.clazz
            clazz = pclazz.loader.load(self.__class_name)
            if not clazz.is_accessible(pclazz):
                raise IllegalAccessException('class {0} not vist class {1} access'.format(pclazz.name, clazz.name))

            self.__clazz = clazz

        return self.__clazz


    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, vars(self))


class ClassRef(SymRef):

    def __init__(self, constant_pool, class_info):
        super(ClassRef, self).__init__(constant_pool, class_info.val)


class MemberRef(SymRef):

    def __init__(self, constant_pool, ref_info):
        super(MemberRef, self).__init__(constant_pool, ref_info.class_name)
        self.__name, self.__descriptor = ref_info.name_and_type


    @property
    def name(self):
        return self.__name


    @property
    def descriptor(self):
        return self.__descriptor


class FieldRef(MemberRef):

    def __init__(self, constant_pool, ref_info):
        super(FieldRef, self).__init__(constant_pool, ref_info)
        self.__field = None


    @classmethod
    def lookup(cls, clazz, name, descriptor):
        for field in clazz.fields:
            if field.name == name and field.descriptor == descriptor:
                return field

        for interface in clazz.interfaces:
            field = cls.lookup(interface, name, descriptor)
            if field:
                return field

        if clazz.super_clazz:
            return cls.lookup(clazz.super_clazz, name, descriptor)

        return None


    @property
    def field(self):
        if self.__field is None:
            pclazz = self.constant_pool.clazz
            clazz = self.clazz

            field = self.lookup(clazz, self.name, self.descriptor)

            if not field.is_accessible(pclazz):
                raise  IllegalAccessException('class {0} not vist field {1}.{2} access'.format(pclazz.name, clazz.name, self.name))
            self.__field = field

        return self.__field



class MethodRef(MemberRef):

    def __init__(self, constant_pool, ref_info):
        super(MethodRef, self).__init__(constant_pool, ref_info)
        self.__method = None


    @property
    def method(self):
        if self.__method is None:
            pclazz = self.constant_pool.clazz
            clazz = self.clazz

            if clazz.is_interface:
                raise IllegalAccessException("method {0}.{1} is interface".format(clazz.name, self.name))

            method = self.lookup(clazz, self.name, self.descriptor)
            if method is None:
                raise IllegalAccessException("method {0}.{1} is not found".format(clazz.name, self.name))

            if not method.is_accessible(pclazz):
                raise IllegalAccessException("class {0} not vist method {1}.{2} access".format(pclazz.name, clazz.name, self.name))
            self.__method = method

        return self.__method


    @classmethod
    def lookup(cls, clazz, name, descriptor):
        method = cls.lookup_in_class(clazz, name, descriptor)
        if method is None:
            method = cls.lookup_in_interfaces(clazz.interfaces, name, descriptor)

        return method


    @classmethod
    def lookup_in_class(cls, clazz, name, descriptor):
        while clazz:
            for method in clazz.methods:
                if name == method.name and descriptor == method.descriptor:
                    return method
            clazz = clazz.super_class
        return None


    @classmethod
    def lookup_in_interfaces(cls, interfaces, name, descriptor):
        for interface in interfaces:
            for method in interface.methods:
                if name == method.name and descriptor == method.descriptor:
                    return method

            method = cls.lookup_in_interfaces(interface.interfaces)
            if method:
                return method

        return None


class InterfaceMethodRef(MethodRef):

    @classmethod
    def lookup(cls, interface, name, descriptor):
        for method in interface.methods:
            if name == method.name and descriptor == method.descriptor:
                return method

        return cls.lookup_in_interfaces(interface.interfaces, name, descriptor)

