import os
from file import File

class Directory:
    def __init__(self, path:str):
        self._path=path

    def traverse(self) -> list:
        items_found=[]
        for inner_path in os.listdir(self._path):
            full_path=os.path.join(self._path,inner_path)
            if os.path.isfile(full_path):
                file_checked = File(full_path)
                items_found.append(file_checked)
            else:
                dir = Directory(full_path)
                items_found.extend(dir.traverse())
        return items_found


    def files_with_content(self,files:list,word:str) ->list:
        files_with_word=[]
        for _file in files:
            if _file.is_word_included(word):
                 files_with_word.append(_file.path)

        return files_with_word





