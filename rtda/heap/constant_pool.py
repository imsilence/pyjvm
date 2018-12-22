#encoding: utf-8

from classfile.constant_info import ConstantUtf8Info, \
                                    ConstantIntegerInfo, ConstantFloatInfo, \
                                    ConstantLongInfo, ConstantDoubleInfo, \
                                    ConstantClassInfo, \
                                    ConstantStringInfo, \
                                    ConstantNameAndTypeInfo, \
                                    ConstantFieldrefInfo, ConstantMethodrefInfo, \
                                    ConstantInterfaceMethodrefInfo

class Constant(object):
    pass


class ConstantPool(object):
    def __init__(self, class_, constant_pool):
        self.__consts = []
        for index in range(0, len(constant_pool)):
            info = constant_pool[index + 1]
            if isinstance(info, (ConstantUtf8Info, ConstantIntegerInfo, ConstantFloatInfo, ConstantLongInfo, ConstantDoubleInfo, ConstantStringInfo)):
                self.__consts.append(info.val)
            elif isinstance(info, ConstantClassInfo):
                pass
            elif isinstance(info, ConstantNameAndTypeInfo):
                pass
            elif isinstance(info, ConstantFieldrefInfo):
                pass
            elif isinstance(info, ConstantMethodrefInfo):
                pass
            elif isinstance(info, ConstantInterfaceMethodrefInfo):
                pass

    def __getitem__(self, index):
        return self.__consts[index - 1]