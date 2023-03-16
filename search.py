

from directory import Directory
from exceptions import FolderNotFoundError
import os

class Search:
    def search_by_content(self, path:str, word:str) -> list:
        if os.path.exists(path):
            dir = Directory(path)
            return dir.files_with_content(word)
        else:
            raise FolderNotFoundError(path)