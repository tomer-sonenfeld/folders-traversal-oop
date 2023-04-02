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
        for name in os.listdir(self._full_path):
            inner_path = os.path.join(self._full_path, name)
            if os.path.isdir(inner_path):
                new_dir = Directory(name, self._full_path)
                files_list.extend(new_dir.list_of_files_in_dirs(word))
            elif os.path.isfile(inner_path):
                new_file = File(inner_path)
                if new_file.is_word_included(word):
                    files_list.append(inner_path)
        return files_list
