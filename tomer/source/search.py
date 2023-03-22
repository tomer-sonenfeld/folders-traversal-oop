

from .directory import Directory
from .exceptions import UnexistedFolder
import os

class Search:
    def search_by_content(self, path:str, word:str) -> list:
        if os.path.exists(path):
            if os.path.isdir(path):
                _dir = Directory(path)
                return set([_file.path for _file in _dir.files_with_content(word)])
            else:
                return path
        else:
            raise UnexistedFolder(path)