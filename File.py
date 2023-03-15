import os

class File:
    def __init__(self,path:str):
        self._path=path


    def include_word(self,word):
        with open(self.path, 'r') as file_opened:
            file_contents = file_opened.read()
            if word in file_contents:
                return True;

        return False

    def my_path(self):
        return self.path

    @property
    def path(self):
        return self._path


    def __str__(self):
        return f"File {self.name} in {self.print_path()}"

    def __repr__(self):
        return f"File \"{self.name}\" in {self.print_path()}"


