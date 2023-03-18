import os


class FailedToCreateDirectory(Exception):
    pass


class FailedToReadFromFile(Exception):
    pass


class Directory(object):
    def __init__(self, path: str, father_directory: 'Directory' = None):
        if not os.path.isdir(path):
            raise FailedToCreateDirectory("path is not a directory")
        self._path = path
        self._father_directory = father_directory
        self._subdirectories = []
        self._files = []

    @property
    def path(self):
        return self._path

    @property
    def father_directory(self):
        return self._father_directory

    @property
    def subdirectories(self):
        return self._subdirectories

    @property
    def files(self):
        return self._files

    def scan_folder(self):
        for item in os.listdir(self._path):
            item_path = os.path.join(self._path, item, "")
            if os.path.isdir(os.path.join(self._path, item)):
                _dir = next((existing_subdir for existing_subdir in self._subdirectories
                             if existing_subdir.path == item_path), None)
                if _dir is None:
                    try:
                        x = Directory(item_path, self)
                        self._subdirectories.append(x)
                    except:
                        pass
                else:
                    _dir.scan_folder()
            elif item_path not in self._files:
                self._files.append(os.path.join(self._path, item))

    def lookup_str_in_files(self, word: str):
        if not os.path.isdir(self._path):
            raise FailedToCreateDirectory("path is no longer a directory")
        self.scan_folder()
        res = []
        for _file in self._files:
            try:
                f = open(_file, "r")
                if word in f:
                    res.append(_file)
            except:
                pass
            finally:
                f.close()
        for _dir in self._subdirectories:
            res.extend(_dir.lookup_str_in_files(word))
        return res
