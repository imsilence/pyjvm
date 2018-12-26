#encoding: utf-8

class Init(object):

    def init_clazz(self, thread, clazz):
        clazz.inited = True
        method = clazz.get_clinit_method()
        if method:
            new_frame = thread.create_frame(method)
            thread.push_frame(new_frame)

        if not clazz.is_interface:
            super_class = clazz.super_class
            if super_class and not super_class.inited:
                self.init_clazz(thread, super_class)
