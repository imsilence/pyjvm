#encoding: utf-8

from enum import Enum

class AccessFlags(Enum):
    PUBLIC = 0X0001         # class field method
    PRIVATE = 0X0002        #       field method
    PROTECTED = 0X0004      #       field method
    STATIC = 0X0008         #       field method
    FINAL = 0X0010          # class field method
    SUPER = 0X0020          # class
    SYNCHRONIZED = 0X0020   #             method
    VOLATILE = 0X0040       #       field
    BRIDGE = 0X0040         #             method
    TRANSIENT = 0X0080      #       field
    VARARGS = 0X0080        #             method
    NATIVE = 0X0100         #             method
    INTERFACE = 0X0200      # class
    ABSTRACT = 0X0400        # class
    STRICT = 0X0800         #             method
    SYNTHETIC = 0X1000      # class field method
    ANNOTATION = 0X2000     # class
    ENUM = 0X4000           # class field


class AccessMixin(object):

    @property
    def is_public(self):
        return 0 != (AccessFlags.PUBLIC.value & self.access_flags)


    @property
    def is_private(self):
        return 0 != (AccessFlags.PRIVATE.value & self.access_flags)


    @property
    def is_protected(self):
        return 0 != (AccessFlags.PROTECTED.value & self.access_flags)


    @property
    def is_static(self):
        return 0 != (AccessFlags.STATIC.value & self.access_flags)


    @property
    def is_final(self):
        return 0 != (AccessFlags.FINAL.value & self.access_flags)


    @property
    def is_super(self):
        return 0 != (AccessFlags.SUPER.value & self.access_flags)


    @property
    def is_synchronized(self):
        return 0 != (AccessFlags.SYNCHRONIZED.value & self.access_flags)


    @property
    def is_volatile(self):
        return 0 != (AccessFlags.VOLATILE.value & self.access_flags)


    @property
    def is_bridge(self):
        return 0 != (AccessFlags.BRIDGE.value & self.access_flags)


    @property
    def is_transient(self):
        return 0 != (AccessFlags.TRANSIENT.value & self.access_flags)


    @property
    def is_varargs(self):
        return 0 != (AccessFlags.VARARGS.value & self.access_flags)


    @property
    def is_native(self):
        return 0 != (AccessFlags.NATIVE.value & self.access_flags)


    @property
    def is_interface(self):
        return 0 != (AccessFlags.INTERFACE.value & self.access_flags)


    @property
    def is_abstract(self):
        return 0 != (AccessFlags.ABSTRACT.value & self.access_flags)


    @property
    def is_strict(self):
        return 0 != (AccessFlags.STRICT.value & self.access_flags)


    @property
    def is_synthetic(self):
        return 0 != (AccessFlags.SYNTHETIC.value & self.access_flags)


    @property
    def is_annotation(self):
        return 0 != (AccessFlags.ANNOTATION.value & self.access_flags)


    @property
    def is_enum(self):
        return 0 != (AccessFlags.ENUM.value & self.access_flags)


