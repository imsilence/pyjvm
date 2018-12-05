#encoding: utf-8

import os

from classpath.class_path import EntryFactory, EntryException

class ClassLoaderException(Exception):
    pass


class ClassLoader(object):

    def __init__(self, jre_path, class_path):
        self.__jre_path = jre_path
        self.__class_path = class_path
        self.__entries = []

        __boot_entry, __ext_entry = self.__init_sys_entries(jre_path)
        __user_entry = self.__init_user_entry(class_path)

        self.__entries.append(__boot_entry)
        self.__entries.append(__ext_entry)
        self.__entries.append(__user_entry)


    def __get_jre_path(self, jre_path):
        if "" != jre_path and os.path.exists(jre_path):
            return jre_path

        if os.path.exists("./jre"):
            return os.path.abspath(".jre")

        java_home = os.environ.get('JAVA_HOME')
        if java_home and os.path.exists(os.path.join(java_home, 'jre')):
            return os.path.join(java_home, 'jre')

        raise EntryException("jre dir not found")

    def __init_sys_entries(self, jre_path):
        jre_path = self.__get_jre_path(jre_path)

        return (EntryFactory.get_entry(os.path.join(jre_path, "lib", "*")),
                EntryFactory.get_entry(os.path.join(jre_path, "lib", "ext", "*")))

    def __init_user_entry(self, class_path):
        class_path = "." if "" == class_path else class_path
        return EntryFactory.get_entry(class_path)

    def read_class(self, class_name):
        class_name = '{0}.class'.format(class_name)
        for entry in self.__entries:
            try:
                return entry.read_class(class_name)
            except EntryException as e:
                pass

        raise ClassLoaderException("class not found: {0}".format(class_name))