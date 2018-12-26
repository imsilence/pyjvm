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
        self.__const_value_index = int(attr.constant_value_index) if attr else 0


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
        self.__signature = None

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


    @property
    def signature(self):
        if self.__signature is None:
            self.__signature = MethodSignature.parse(self)

        return self.__signature


class MethodSignature(object):

    def __init__(self, method):
        self.__method = method
        self.__param_types = []
        self.__return_type = None


    @classmethod
    def parse(self, method):
        signature = MethodSignature(method)

        param_desc, return_desc = method.descriptor.split(')')

        signature.__return_type = return_desc

        param_desc = param_desc[1:]

        param_type = []

        while param_desc:
            _pox = 0
            if param_desc[0] == 'L':
                _pox = param_desc.find(';')
                param_type.append(param_desc[1:_pox])
                signature.__param_types.append(''.join(param_type))
                param_type = []
            elif param_desc[0] == '[':
                param_type.append('[')
            else:
                param_type.append(param_desc[0])
                signature.__param_types.append(''.join(param_type))
                param_type = []

            param_desc = param_desc[_pox + 1:]

        return signature


    @property
    def param_types(self):
        return self.__param_types


    @property
    def return_type(self):
        return self.__return_type


    @property
    def var_count(self):
        return len(self.param_types) + 1 if self.__method.is_static else 0


    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, vars(self))

