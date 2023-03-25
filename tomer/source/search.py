

from .directory import Directory
from .exceptions import NonExistingPathError
import os

class Search:
    def search_by_content(self, path:str, word:str) -> list:
        if not os.path.exists(path):
            raise NonExistingPathError(path)

        if os.path.isdir(path):
                _dir = Directory(path)
                return _dir.files_with_content(word)

        elif os.path.isfile(path):
            return path

        else:
            print("Unsupported path type")