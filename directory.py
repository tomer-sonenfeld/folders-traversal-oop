import os
import directory
from file import File


class NotADirectoryErr(Exception):
    pass


class Directory:

    def __init__(self, name: str, parent_path: str = ""):
        self._name = name
        self._parent_path = parent_path
        self._full_path = os.path.join(parent_path, name)

        if not os.path.isdir(self._full_path):
            raise NotADirectoryErr()

    def list_dirs(self, word: str):
        files_list = []
        my_path = self._full_path
        for name in os.listdir(my_path):
            tmp_path = os.path.join(my_path, name)
            if os.path.isdir(tmp_path):
                new_dir = Directory(name, my_path)
                files_list.extend(new_dir.list_dirs(word))
            elif os.path.isfile(tmp_path):
                self._check_word_in_file(tmp_path, word, files_list)
        return files_list

    def _check_word_in_file(self, my_path: str, word: str, files_list: list):
        new_file = File(my_path)
        if new_file.find_word(word):
            files_list.append(my_path)

    if __name__ == '__main__':
        dir = directory.Directory("D:\PycharmProjects\pypy")
        print(dir.list_dirs('shir'))