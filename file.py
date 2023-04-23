import os.path


class File:
    def __init__(self, fullpath: str):
        self._fullpath = fullpath

    def word_match(self, word: str):
        try:
            with open(self._fullpath, "r") as _file:
                return word in _file.read()
        except UnicodeDecodeError:
            return False


# return iterator of all words in file, none if open fails
    @classmethod
    def from_path(cls, fullpath: str):
        if os.path.isfile(fullpath):
            return cls(fullpath)
        return None

    def __getattr__(self, item):
        try:
            super().__getattribute__(item)
        except AttributeError:
            return self.word_match(item)

    # @classmethod
    # def calculate_age(cls, name, birth_year):
    #     # calculate age an set it as a age
    #     # return new object
    #     return cls(name, date.today().year - birth_year)
