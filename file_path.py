import os.path


class PathIsNotAFile(Exception):
    pass


class File:
    def __init__(self, fullpath: str):
        self._fullpath = fullpath

    def word_match(self, word: str):
        try:
            with open(self._fullpath, "r") as _file:
                return word in _file.read()
        except UnicodeDecodeError:
            return False

    @classmethod
    def check_path(cls, fullpath: str):
        try:
            assert os.path.isfile(fullpath)
            return True
        except AssertionError:
            return False

    def __getattr__(self, item):
        try:
            super().__getattribute__(item)
        except AttributeError:
            return self.word_match(item)

