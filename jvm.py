#encoding: utf-8

from classpath import ClassPath
from rtda.heap import ClassLoader
from interpreter import interpret

class JVM(object):

    def __init__(self, cmd):
        self.__cmd = cmd
        self.__class_path = ClassPath(cmd.jre_path, cmd.class_path)


    def start(self):

        class_loader = ClassLoader(self.__class_path)
        clazz = class_loader.load(self.__cmd.clazz)
        main_method = clazz.get_main_method()

        if main_method:
            interpret(main_method)
