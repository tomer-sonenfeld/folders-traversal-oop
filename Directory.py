import os
from File import File

class Directory:
    def __init__(self, path:str):
        self._path=path
        self._my_files=[]

    def traverse(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                self.my_files.append(os.path.join(root, file))
        return self.my_files

    def files_with_content(self,word:str):
        files_with_word=[]
        for file in self.my_files:
            if os.path.isfile(file) and file.endswith('.txt'):
                file_checked = File(file)
                if file_checked.include_word(word):
                    files_with_word.append(file_checked.my_path())

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

    def __str__(self):
        return f"Folder {self.name} in {self.print_path()}"
    def __repr__(self):
        return f"Folder \"{self.name}\" in {self.print_path()}"

