#encoding: utf-8

from native.base import Method
from native.method import register
from rtda.heap import StringFactory
from native.exceptions import MethodException

class StrackTraceElement(object):

    def __init__(self, file_name, class_name, method_name, line_number):
        self.__file_name = ''
        self.__class_name = ''
        self.__method_name = ''
        self.__line_number = 0


    def __repr__(self):
        return '{0}|{1}.{2} line:{3}'.format(self.__file_name, self.__class_name, self.__method_name, self.__line_number)


@register(class_name="java/lang/Throwable", method_name="fillInStackTrace", descriptor="(I)Ljava/lang/Throwable;")
class MethodFillInStackTrace(Method):

    @classmethod
    def execute(cls, frame):
        this = frame.vars[0]
        print(this.clazz.name)
        frame.stack.push(this)

        traces = []

        for frame in frame.thread.frames:
            method = frame.method
            print(type(method))
            clazz = method.clazz
            traces.append(StrackTraceElement(
                clazz.source_file,
                clazz.java_name,
                method.name,
                method.find_line_number(frame.next_pc - 1)
            ))

        this.extra = traces