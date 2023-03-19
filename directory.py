

import os
from file import File

class Directory:
    def __init__(self, path:str):
        self._path=path

    def traverse(self) -> list:
        files_found=[]
        for inner_path in os.listdir(self._path):
            full_path=os.path.join(self._path,inner_path)
            if os.path.isfile(full_path):
                _file = File(full_path)
                files_found.append(_file)
            elif os.path.isdir(full_path):
                sub_dir = Directory(full_path)
                files_found.extend(sub_dir.traverse())
        return files_found


    def files_with_content(self,word:str) -> list:
        files_found=self.traverse()
        files_with_word=[]
        for _file in files_found:
                if _file.is_word_included(word):
                    files_with_word.append(_file.path)
        return files_with_word







