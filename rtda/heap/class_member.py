#encoding: utf-8


from .access_flags import AccessMixin


class ClassMember(AccessMixin):

    def __init__(self, clazz, member):
        self.__access_flags = int(member.access_flags)
        self.__name = member.name
        self.__descriptor = member.descriptor
        self.__clazz = clazz


    @property
    def access_flags(self):
        return self.__access_flags


    @property
    def name(self):
        return self.__name


    @property
    def descriptor(self):
        return self.__descriptor


    @property
    def clazz(self):
        return self.__clazz


    def is_accessible(self, clazz):
        if self.is_public:
            return True

        if self.is_protected:
            return clazz == self.__clazz or \
                    clazz.is_subclass(self.__clazz) or \
                    clazz.package_name == self.__clazz.package_name

        if not self.is_private:
            return clazz.package_name == self.__clazz.package_name

        return clazz == self.__clazz

    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, vars(self))


class ClassField(ClassMember):

    def __init__(self, clazz, member):
        super(ClassField, self).__init__(clazz, member)

        attr = member.constant_value_attr

        self.__index = 0
        self.__const_value_index = attr.constant_value_index if attr else 0


    @property
    def index(self):
        return self.__index


    @index.setter
    def index(self, index):
        self.__index = index


    @property
    def const_value_index(self):
        return self.__const_value_index


class ClassMethod(ClassMember):

    def __init__(self, clazz, method):
        super(ClassMethod, self).__init__(clazz, method)
        self.__max_stack = 0
        self.__max_locals = 0
        self.__code = b''

        if method.code_attr:
            self.__max_stack = method.code_attr.max_stack
            self.__max_locals = method.code_attr.max_locals
            self.__code = method.code_attr.code.byte


    @property
    def max_stack(self):
        return self.__max_stack


    @property
    def max_locals(self):
        return self.__max_locals


    @property
    def code(self):
        return self.__code



