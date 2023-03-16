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
                #self._my_files.append(file_checked)
                items_found.append(file_checked)
            else:
                dir = Directory(os.path.join(self._path,inner_path))
                items_found.extend(dir.traverse())
        self._files_in_directory.extend(items_found)
        return items_found


    def files_with_content(self,word:str):
        files_with_word=[]
        for file in self._files_in_directory:
                if file.include_word(word):
                    files_with_word.append(file.my_path())

        return files_with_word

    @property
    def my_files(self):
        return self._files_in_directory

    @property
    def path(self):
        return self._path




    def __getattr__(self, attr:str):
        try:
            for folder in self._contents:
                if folder._name == attr:
                    return folder
            return super().__getattribute__(attr)
        except AttributeError as e:
            raise e

