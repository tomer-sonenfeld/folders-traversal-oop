import os
import directory
from file import File


class Directory:

    def __init__(self, name: str, parent_path: str = ""):
        self._name = name
        self._parent_path = parent_path
        self._full_path = os.path.join(parent_path, name)

    def list_dirs(self, word: str, files_list: list):
        my_path = self._full_path
        if os.path.isdir(my_path):
            for name in os.listdir(my_path):
                tmp_path = os.path.join(my_path, name)
                if os.path.isdir(tmp_path):
                    new_dir = Directory(name, my_path)
                    new_dir.list_dirs(word, files_list)
                elif os.path.isfile(tmp_path):
                    self.check_word_in_file(tmp_path, word, files_list)
        elif os.path.isfile(my_path):
            self.check_word_in_file(my_path, word, files_list)

    def check_word_in_file(self, my_path: str, word: str, files_list: list):
        new_file = File(my_path)
        if new_file._find_word(word):
            files_list.append(my_path)

    if __name__ == '__main__' :
        dir = directory.Directory("D:\PycharmProjects\pypy")
        output_files = []
        dir.list_dirs('shir', output_files)
        print(output_files)



