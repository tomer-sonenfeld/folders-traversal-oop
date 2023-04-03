import os
from file import File


class Directory:

    def __init__(self, name: str, parent_path: str = ""):
        self._name = name
        self._parent_path = parent_path
        self._full_path = os.path.join(parent_path, name)

        if not os.path.isdir(self._full_path):
            raise NotADirectoryError

    def list_of_files_in_dirs(self, word: str) -> list:
        files_list = []
        for relative_path in os.listdir(self._full_path):
            full_path = os.path.join(self._full_path, relative_path)
            if os.path.isdir(full_path):
                _dir = Directory(relative_path, self._full_path)
                files_list.extend(_dir.list_of_files_in_dirs(word))
            elif os.path.isfile(full_path):
                _file = File(full_path)
                if _file.is_word_included(word):
                    files_list.append(full_path)
        return files_list
