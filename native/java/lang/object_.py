#encoding: utf-8

from native.base import Method
from native.method import register
from rtda.heap import StringFactory

@register(class_name="java/lang/Object", method_name="getClass", descriptor="()Ljava/lang/Class;")
class MethodGetClass(Method):

    @classmethod
    def execute(cls, frame):
        this = frame.vars[0]
        clazz = this.clazz.base_class
        frame.stack.push(clazz)


@register(class_name="java/lang/Class", method_name="getPrimitiveClass", descriptor="(Ljava/lang/String;)Ljava/lang/Class;")
class MethodGetPrimitiveClass(Method):

    @classmethod
    def execute(cls, frame):
        name_obj = frame.vars[0]

        name = StringFactory.object_2_string(frame.vars[0])

        loader = frame.method.clazz.loader
        clazz = loader.load(name).base_class

        frame.stack.push(clazz)


@register(class_name="java/lang/Class", method_name="getName0", descriptor="()Ljava/lang/String;")
class MethodGetName0(Method):

    @classmethod
    def execute(cls, frame):
        this = frame.vars[0]
        clazz = this.extra

        frame.stack.push(StringFactory.get(clazz.loader,  clazz.java_name))


@register(class_name="java/lang/Class", method_name="desiredAssertionStatus0", descriptor="(Ljava/lang/Class;)Z")
class MethodDesiredAssertionStatus0(Method):

    @classmethod
    def execute(cls, frame):
        frame.stack.push(False)