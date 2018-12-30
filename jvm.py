#encoding: utf-8

from classpath import ClassPath
from rtda.heap import ClassLoader, StringFactory
from interpreter import Interpreter
from rtda import Thread

class JVM(object):

    def __init__(self, cmd):
        self.__cmd = cmd


    def start(self):
        cmd = self.__cmd

        class_loader = ClassLoader(ClassPath(cmd.jre_path, cmd.class_path))
        main_thread = Thread()
        interpreter = Interpreter(main_thread)

        clazz = class_loader.load("sun/misc/VM")
        interpreter.interpret()

        clazz = class_loader.load(cmd.clazz)

        main_method = clazz.get_main_method()
        if main_method is None:
            raise Exception("not found main method in class {0}".format(clazz.name))

        frame = main_thread.create_frame(main_method)
        frame.vars[0] = self.__get_args(class_loader)
        main_thread.push_frame(frame)
        interpreter.interpret()


    def __get_args(self, class_loader):
        args = self.__cmd.args

        clazz = class_loader.load('java/lang/String')
        array = clazz.array_class.create_array_object(len(args))

        for index, arg in enumerate(args):
            array.fields[index] = StringFactory.get(class_loader, arg)

        return array