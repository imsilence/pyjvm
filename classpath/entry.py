#encoding: utf-8

from abc import ABC, abstractmethod
import os
from zipfile import ZipFile

class EntryException(Exception):
    pass


class EntryFactory(object):

    @classmethod
    def get_entry(cls, path):
        if os.pathsep in path:
            return CompositeEntry(path)
        elif "*" in path:
            return WildcardEntry(path)
        elif str(os.path.splitext(path)[-1]).lower() in ['.jar', '.zip']:
            return ZipEntry(path)
        else:
            return DirEntry(path)


class Entry(ABC):

    @abstractmethod
    def read_class(self, class_name):
        pass

    def __repr__(self):
        return '<{0!r}>{1!r}'.format(self.__class__.__name__, vars(self))


class DirEntry(Entry):

    def __init__(self, path):
        self.__dir_path = os.path.abspath(path)

    def read_class(self, class_name):
        path = os.path.join(self.__dir_path, class_name)

        if not os.path.exists(path):
            raise EntryException("class file not found: {0}".format(path))

        with open(path, "rb") as fhandler:
            return fhandler.read()


class ZipEntry(Entry):

    def __init__(self, path):
        self.__zip_path = os.path.abspath(path)

    def read_class(self, class_name):
        path = self.__zip_path
        if not os.path.exists(path):
            raise EntryException("zip/jar file not found: {0}".format(path))

        zf = None
        try:
            zf = ZipFile(path)
            if class_name not in zf.namelist():
                raise EntryException("class file not found, class: {0}, path: {1}".format(class_name, path))

            return zf.read(class_name)
        finally:
            if zf:
                zf.close()


class CompositeEntry(Entry):

    def __init__(self, path):
        self.__path = path
        self.__entries = self.__init_entries(path.split(os.pathseq))

    def __init_entries(self, paths):
        entries = []
        for path in paths:
            entries.append(EntryFactory.get_entry(path))
        return entries

    def read_class(self, class_name):
        for entry in self.__entries:
            try:
                return entry.read_class(class_name)
            except EntryException as e:
                pass

        raise EntryException("class file not found, class: {0}, path: {1}".format(class_name, self.__path))


class WildcardEntry(Entry):

    def __init__(self, path):
        self.__path = path
        self.__entries = self.__init__entries(path[:len(path) - 1])

    def __init__entries(self, path):
        if not os.path.exists(path):
            raise EntryException("dir path not found: {0}".format(path))

        entries = []
        for fname in os.listdir(path):
            fpath = os.path.join(path, fname)

            if not os.path.isfile(fpath):
                continue

            if str(os.path.splitext(fpath)[-1]).lower() not in ['.jar', '.zip']:
                continue

            entries.append(ZipEntry(fpath))

        return entries


    def read_class(self, class_name):
        for entry in self.__entries:
            try:
                return entry.read_class(class_name)
            except EntryException as e:
                pass

        raise EntryException("class file not found, class: {0}, path: {1}".format(class_name, self.__path))


