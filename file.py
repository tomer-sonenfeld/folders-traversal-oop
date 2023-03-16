import os

class File:
    def __init__(self,path:str):
        self._path=path


    def is_word_included(self, word) -> bool:
        with open(self._path, 'r') as file_opened:
            content = file_opened.read()
        return word in content

    @property
    def path(self):
        return self._path




