

import os
from file import File

class Directory:
    def __init__(self, path:str):
        self._path=path

    def _traverse(self) -> list:
        items_found=[]
        for inner_path in os.listdir(self._path):
            full_path=os.path.join(self._path,inner_path)
            if os.path.isfile(full_path):
                _file = File(full_path)
                items_found.append(_file)
            elif os.path.isdir(full_path):
                dir = Directory(full_path)
                items_found.extend(dir._traverse())
        return items_found


    def files_with_content(self,word:str) -> list:
        files_found=self._traverse()
        files_with_word=[]
        for _file in files_found:
            try:
                if _file.is_word_included(word):
                    files_with_word.append(_file.path)
            except:
                print(f"Could'nt read file {_file.path} because of coding exception")

        return files_with_word





