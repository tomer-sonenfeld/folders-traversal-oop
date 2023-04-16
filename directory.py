import os
import file
from typing import List

class FailedToCreateDirectory(Exception):
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

    def _sub_dir_already_registered(self, new_subdir) -> bool:
        for subdir in self._subdirectories:
            if subdir.path == new_subdir:
                return True
        return False

    def _file_already_registered(self, file_path: str) -> bool:
        for _file in self._files:
            if _file.path == file_path:
                return True
        return False

    def _scan_folder(self):
        for relative_path in os.listdir(self._path):
            full_path = os.path.join(self._path, relative_path)
            if os.path.isdir(full_path):
                if not self._sub_dir_already_registered(full_path):
                    continue
                try:
                    new_subdir = Directory(full_path)
                    self._subdirectories.append(new_subdir)
                except FailedToCreateDirectory:
                    print(f'Failed to create directory: {full_path}')
            elif os.path.isfile(full_path) and not self._file_already_registered(full_path):
                self._files.append(file.File(full_path))

    def lookup_str_in_files(self, word: str) -> List[str]:
        if not os.path.isdir(self._path):
            print(f'Directory {self._path} no longer exists.')
            return
        self._scan_folder()
        res = []
        for _file in self._files:
            if _file.lookup_str_in_file(word):
                res.append(_file.path)
        for _dir in self._subdirectories:
            res.extend(_dir.lookup_str_in_files(word))
        return res
