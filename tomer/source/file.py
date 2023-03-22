

class File:
    def __init__(self,path:str):
        self._path=path


    def _is_word_included(self, word:str) -> bool:
        with open(self._path, 'r') as _file:
            try:
                content = _file.read()
            except UnicodeDecodeError:
                return False
        return word in content

    @property
    def path(self):
        return self._path

    def __repr__(self):
        return self._path




