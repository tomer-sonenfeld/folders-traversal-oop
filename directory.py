import os
from file import File

class Directory:
    def __init__(self, path:str):
        self._path=path
        self._files_in_directory=[]

    def traverse(self):
        items_found=[]
        for inner_path in os.listdir(self._path):
            if os.path.isfile(os.path.join(self._path,inner_path)):
                file_checked = File(os.path.join(self._path,inner_path))
                items_found.append(file_checked)
            else:
                dir = Directory(os.path.join(self._path,inner_path))
                items_found.extend(dir.traverse())
        self._files_in_directory.extend(items_found)
        return items_found


    def files_with_content(self,word:str):
        files_with_word=[]
        for file in self._files_in_directory:
                if file.is_word_included(word):
                    files_with_word.append(file.path)

        return files_with_word





