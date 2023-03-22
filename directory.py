import os


class FailedToCreateDirectory(Exception):
    pass


class FailedToReadFromFile(Exception):
    pass


class Directory(object):
    def __init__(self, path: str):
        if not os.path.isdir(path):
            raise FailedToCreateDirectory("path is not a directory")
        self._path = path
        self._subdirectories = []
        self._files = []

    @property
    def path(self):
        return self._path

    def _scan_folder(self):
        for relative_path in os.listdir(self._path):
            full_path = os.path.join(self._path, relative_path)
            if os.path.isdir(full_path):
                sub_dir_exists = False
                for sub_dir in self._subdirectories:
                    if sub_dir.path == full_path:
                        sub_dir_exists = True
                        break
                if not sub_dir_exists:
                    try:
                        new_subdir = Directory(full_path)
                        self._subdirectories.append(new_subdir)
                    except FailedToCreateDirectory:
                        print(f'Failed to create directory: {full_path}')
            elif full_path not in self._files:
                self._files.append(full_path)

    def lookup_str_in_files(self, word: str):
        if not os.path.isdir(self._path):
            print(f'Directory {self._path} no longer exists.')  # Should I print the error?
            return
        self._scan_folder()
        res = []
        for _file in self._files:
            try:
                with open(_file) as file_object:
                    if word in file_object.read():
                        res.append(_file)
            except OSError:
                print(f"Failed to open file: {_file}")
        for _dir in self._subdirectories:
            res.extend(_dir.lookup_str_in_files(word))
        return res
