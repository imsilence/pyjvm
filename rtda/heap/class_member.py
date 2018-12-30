#encoding: utf-8


from .access_flags import AccessMixin
from .exception_table import ExceptionTableEntry


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
        self.__exception_table = []
        self.__line_number_table = []

        if method.code_attr:
            self.__max_stack = method.code_attr.max_stack
            self.__max_locals = method.code_attr.max_locals
            self.__code = method.code_attr.code.byte
            self.__exception_table = [ExceptionTableEntry(self, clazz.constant_pool, exception) for exception in  method.code_attr.exceptions]
            self.__line_number_table = method.code_attr.line_number_table

        if self.is_native:
            self.__inject()


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


    def __inject(self):
        codes = {
            'V' : b'\xfe\xb1', # return
            'D' : b'\xfe\xaf', # dreturn
            'F' : b'\xfe\xae', # freturn
            'J' : b'\xfe\xad', # lreturn
            'L' : b'\xfe\xb0', # areturn
        }


        default_code = b'\xfe\xac' # ireturn
        signature = self.signature

        self.__max_stack = 4
        self.__max_locals = signature.var_count + 1
        self.__code = codes.get(signature.return_type, default_code)


    def find_exception_handler(self, exception, pc):
        for entry in self.__exception_table:
            if entry.start_pc <= pc and entry.end_pc >= pc:
                if entry.catch_type is None:
                    return entry.handler_pc
                else:
                    clazz = entry.catch_type.clazz
                    if clazz == exception or clazz.is_superclass(exception):
                        return entry.handler_pc

        return -1


    def find_line_number(self, pc):
        if self.is_native:
            return -2

        for line in self.__line_number_table[::-1]:
            if pc >= line.start_pc:
                return line.line_number
        return -1


class MethodSignature(object):

    def __init__(self, method):
        self.__method = method
        self.__param_types = []
        self.__return_type = None


    @classmethod
    def parse(self, method=None, descriptor=None):
        signature = MethodSignature(method)

        descriptor = method.descriptor if method else descriptor

        param_desc, return_desc = descriptor.split(')')

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
        return len(self.param_types) if self.__method.is_static else len(self.param_types) + 1


    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, vars(self))

