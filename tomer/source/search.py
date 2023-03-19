

from .directory import Directory
from .exceptions import FolderNotFoundError
import os

class Search:
    def search_by_content(self, path:str, word:str) -> list:
        if os.path.exists(path):
            _dir = Directory(path)
            return set([f.path for f in _dir.files_with_content(word)])
        else:
            raise FolderNotFoundError(path)