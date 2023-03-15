import os
from training import file


class NotDirInstance(Exception):
    pass


class Dir:
    def __init__(self, path: str, parent: object = None):
        self._path = path

        if parent is None:
            self._parent = None
        elif isinstance(parent, Dir):
            self._parent = parent
        else:
            return NotDirInstance

        self._fullpath = ""

    def __getattr__(self, item):
        if item in os.listdir(self.full_path()):
            return Dir(item, self)
        try:
            return super().__getattribute__(item)
        except AttributeError:
            return self.match_files(item)

    def full_path(self):
        if self._fullpath == "":
            if self._parent is None:
                self._fullpath = os.path.join("", self._path)
            else:
                self._fullpath = os.path.join(self._parent.full_path(), self._path)
        else:
            return self._fullpath

    def match_files(self, word):
        matched_file_paths = []
        for path in os.listdir(self.full_path()):
            sub_dir = Dir(path, self)
            if os.path.isdir(sub_dir.full_path()):
                matched_file_paths += sub_dir.match_files(word)

            elif os.path.isfile(sub_dir.full_path()):
                f = file.File(sub_dir)
                if f.word_match(word):
                    matched_file_paths.append(sub_dir.full_path())

        return matched_file_paths

