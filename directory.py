import os
from file import File

class Directory:
    def __init__(self, path:str):
        self._path=path
        self._my_files=[]

    def traverse(self):
        for item in os.listdir(self._path):
            if os.path.isfile(self._path+"\\"+item):
                file_checked = File(self._path+"\\"+item)
                self._my_files.append(file_checked)
            else:
                dir = Directory(self._path+"\\"+item)
                dir.traverse()
                self.my_files.extend(dir._my_files)


    def files_with_content(self,word:str):
        files_with_word=[]
        for file in self._my_files:
                if file.include_word(word):
                    files_with_word.append(file.my_path())

        return files_with_word

    @property
    def my_files(self):
        return self._my_files

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

