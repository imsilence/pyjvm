#encoding: utf-8

from argparse import ArgumentParser

class Cmd(object):

    __parser = None

    def __init__(self, help_flag=False, version_flag=False, class_path="", jre_path="", args=None):
        self.__help_flag = help_flag
        self.__version_flag = version_flag
        self.__class_path = class_path
        self.__jre_path = jre_path
        self.__clazz = args[0] if isinstance(args, list) and args else ''
        self.__args = args[1:] if isinstance(args, list) and args else []

    @property
    def help_flag(self):
        return self.__help_flag

    @property
    def version_flag(self):
        return self.__version_flag

    @property
    def class_path(self):
        return self.__class_path

    @property
    def jre_path(self):
        return self.__jre_path

    @property
    def clazz(self):
        return self.__clazz

    @property
    def args(self):
        return self.__args

    @classmethod
    def parser(cls):
        if cls.__parser is not None:
            return cls.__parser

        parser = ArgumentParser(prog="pyjvm", usage="python pyjvm [-cp CLASSPATH] class [args ...]", add_help=False)
        parser.add_argument("-?", "-h", dest="help", action="store_true", help="print help and exit")
        parser.add_argument("-v", "-version", dest="version", action="store_true",  help="print version and exit")
        parser.add_argument("-cp", "-classpath", dest="class_path", type=str, default="", help="class path")
        parser.add_argument("-Xjre", dest="jre_path", type=str, default="", help="jre path")
        parser.add_argument("args", type=str, nargs="*", help="args")
        cls.__parser = parser
        return parser

    @classmethod
    def parse(cls, argv):
        parser = cls.parser()
        args = parser.parse_args(argv)
        return cls(args.help, args.version, args.class_path, args.jre_path, args.args)

    def help(self):
        parser = self.parser()
        parser.print_help()

    def version(self):
        print("Version 1.0")

    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, vars(self))