#encoding: utf-8

from ..exceptions import InstructionException

class InvokeMixin(object):

    def invoke_method(self, frame, method):

        thread = frame.thread
        new_frame = thread.create_frame(method)
        thread.push_frame(new_frame)

        for idx in range(method.signature.var_count - 1, -1, -1):
            new_frame.vars[idx] = frame.stack.pop()


