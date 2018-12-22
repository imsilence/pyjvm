#encoding: utf-8

from classpath import ClassPath
from classfile import ClassFile
from interpreter import interpret

class JVM(object):

    def __init__(self, cmd):
        self.__cmd = cmd
        self.__class_path = ClassPath(cmd.jre_path, cmd.class_path)


    def start(self):
        class_file = ClassFile.parse(self.__class_path.read_class(self.__cmd.clazz))

        print('version: ', class_file.version)

        print('constant pool length: ', len(class_file.constant_pool))

        for idx, constant in enumerate(class_file.constant_pool.infos, start=1):
            print('\t', idx, constant)

        print('access flags: ', class_file.access_flags)
        print('class name: ', class_file.class_name)
        print('super class name: ', class_file.super_class_name)

        print('interfaces: ', len(class_file.interface_names))
        for idx, interface in enumerate(class_file.interface_names):
            print('\t', idx, interface)

        print('fields: ', len(class_file.fields))
        for idx, field in enumerate(class_file.fields):
            print('\t', idx, field)
            for idx, attr in enumerate(field.attrs):
                print('\t\t', idx, attr)

        print('methods: ', len(class_file.methods))
        main_method = None
        for idx, method in enumerate(class_file.methods):
            print('\t', idx, method)
            if method.name == 'main' and method.descriptor == '([Ljava/lang/String;)V':
                main_method = method
            for idx, attr in enumerate(method.attrs):
                print('\t\t', idx, attr)

        print('attrs: ', len(class_file.attrs))
        for idx, attr in enumerate(class_file.attrs):
            print('\t', idx, attr)

        if main_method:
            interpret(main_method)
