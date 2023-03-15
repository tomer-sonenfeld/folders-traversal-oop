import os


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
            raise NotDirInstance

        if parent is None:
            self._fullpath = os.path.join("", path)
        else:
            self._fullpath = os.path.join(parent._fullpath, path)

    def __getattr__(self, item):
        if item in os.listdir(self._fullpath):
            return Dir(item, self)
        try:
            super().__getattribute__(item)
        except AttributeError:
            return self.match_files(item)

    def match_files(self, word):
        matched_file_paths = []
        for path in os.listdir(self._fullpath):
            sub_dir = Dir(path, self)
            if os.path.isdir(sub_dir._fullpath):
                matched_file_paths += sub_dir.match_files(word)

            elif os.path.isfile(sub_dir._fullpath):
                f = File(sub_dir._path, sub_dir._parent)
                if f.word_match(word):
                    matched_file_paths.append(sub_dir._fullpath)

        return matched_file_paths


class PathIsNotAFile(Exception):
    pass


class File(Dir):
    def __init__(self, file_name: str, parent: Dir):
        super().__init__(file_name, parent)
        if not os.path.isfile(self._fullpath):
            raise PathIsNotAFile

    def word_match(self, word):
        try:
            with open(self._fullpath, "r") as file:
                return word in file.read()
        except UnicodeDecodeError:
            return False
