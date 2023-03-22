import os
from File import File

class Directory:
    def __init__(self, name: str, parent_path: str):
        self._name = name
        self._parent_path = parent_path
        self._full_path = os.path.join(parent_path, name)

    def list_dirs(self, word: str, files_list: list):
        my_path = self._full_path
        if os.path.isfile(my_path):
            new_file = File(my_path)
            if new_file.find_word(word):
                files_list.append(my_path)
        elif os.path.isdir(my_path):
            for file in os.listdir(my_path):
                new_dir = Dir(file, my_path)
                new_dir.list_dirs(word, files_list)

