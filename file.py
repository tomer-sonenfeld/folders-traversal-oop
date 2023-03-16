

class File:
    def __init__(self,path:str):
        self._path=path


    def is_word_included(self, word:str) -> bool:
        with open(self._path, 'r') as _file:
            content = _file.read()
        return word in content

    @property
    def path(self):
        return self._path




