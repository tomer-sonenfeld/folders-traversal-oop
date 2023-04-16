import os


class File(object):
    def __init__(self, path:str):
        if not os.path.isfile(path):
            raise Exception("path is not a file")
        self._path = path

    @property
    def path(self):
        return self._path

    def lookup_str_in_file(self, word: str):
        try:
            with open(self._path) as file_object:
                if word in file_object.read():
                    return True
            return False
        except OSError:
            print(f"Failed to open file: {self._path}")
