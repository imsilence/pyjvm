#encoding: utf-8

from class_loader import ClassLoader
from class_file import ClassFile

class JVM(object):

    def __init__(self, cmd):
        self.__cmd = cmd
        self.__class_loader = ClassLoader(cmd.jre_path, cmd.class_path)


    def start(self):
        class_file = ClassFile.parse(self.__class_loader.read_class(self.__cmd.clazz))

        print(class_file.version)
        print(class_file.class_name)
        print(class_file.super_class_name)
        print(len(class_file.constant_pool))
        print(class_file.interface_names)
        print(class_file.fields)
        print(class_file.methods)