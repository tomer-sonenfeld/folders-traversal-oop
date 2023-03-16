import os

class File:
    def __init__(self,path:str):
        self._path=path


    def is_word_included(self, word):
        with open(self._path, 'r') as file_opened:
            file_contents = file_opened.read()
        return word in file_contents

    @property
    def path(self):
        return self._path




