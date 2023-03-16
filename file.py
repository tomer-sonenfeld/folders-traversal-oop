import os

class File:
    def __init__(self,path:str):
        self._path=path


    def is_word_included(self, word) -> bool:
        with open(self._path, 'r') as _file:
            file_contents = _file.read()
        return word in file_contents

    @property
    def path(self):
        return self._path




