import os
from training.file_path import File


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
            sub_dir = Dir(path, self)
            if os.path.isdir(sub_dir.fullpath):
                matched_file_paths += sub_dir.match_files(word)

            elif File.check_path(sub_dir.fullpath):
                path_file = File(sub_dir.fullpath)
                if path_file.word_match(word):
                    matched_file_paths.append(sub_dir.fullpath)

        return matched_file_paths

    def __repr__(self):
        return self._fullpath

