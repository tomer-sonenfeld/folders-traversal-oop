

from .directory import Directory
from .exceptions import NonExistingPathError
from .file import File
import os


class Search:
    def search_by_content(self, path: str, word: str) -> set:
        if not os.path.exists(path):
            raise NonExistingPathError(path)

        if os.path.isdir(path):
            _dir = Directory(path)
            return _dir.files_with_content(word)

        elif os.path.isfile(path):
            _file = File(path)
            if _file.is_word_included(word):
                return {_file.path}
            else:
                return set()

        else:
            print("Unsupported path type")
