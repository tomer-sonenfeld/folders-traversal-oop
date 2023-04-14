import os
from training.file import File


class InvalidDirPathException(Exception):
    pass


class Dir:
    def __init__(self, path: str, parent: object = None):
        self._path = path

        if isinstance(parent, Dir):
            self._parent = parent
            self._fullpath = os.path.join(parent._fullpath, path)
        else:
            print("Parent is not dir instance")
            self._parent = None
            self._fullpath = os.path.join("", path)

        if not os.path.isdir(self._fullpath):
            raise InvalidDirPathException

    @property
    def path(self):
        return self._path

    @property
    def fullpath(self):
        return self._fullpath

    @property
    def parent(self):
        return self._parent

    def __getattr__(self, item):
        if item in os.listdir(self._fullpath):
            return Dir(item, self)
        try:
            super().__getattribute__(item)
        except AttributeError:
            return self.match_files(item)

    def match_files(self, word: str):
        matched_file_paths = []
        for path in os.listdir(self._fullpath):
            sub_dir = Dir.from_path(path, self)
            if sub_dir is not None:
                matched_file_paths += sub_dir.match_files(word)
            else:
                path_file = File.from_path(os.path.join(self.fullpath, path))
                if path_file is not None:
                    matched_file_paths += [os.path.join(self.fullpath, path)] if path_file.word_match(word) else []
        return matched_file_paths

    def __repr__(self):
        return self._fullpath

    @classmethod
    def from_path(cls, path: str, parent: object = None):
            if isinstance(parent, Dir):
                fullpath = os.path.join(parent._fullpath, path)
            else:
                fullpath = os.path.join("", path)

            if os.path.isdir(fullpath):
                return Dir(path, parent)