#encoding: utf-8

from ..exceptions import InstructionException

class InvokeMixin(object):

    def invoke_method(self, frame, method):

        thread = frame.thread
        new_frame = thread.create_frame(method)
        thread.push_frame(new_frame)
        param_types = method.signature.param_types
        for idx in range(len(param_types) - 1, -1, -1):
            new_frame.vars[idx] = frame.stack.pop()

        if method.is_native:
            if method.name == 'registerNatives':
                thread.pop_frame()
            else:
                raise InstructionException('method {0}.{1} is native'.format(method.clazz.name, method.name))