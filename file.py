import os
class File:

    def __init__(self, full_path: str):
        self._full_path = full_path

    def _find_word(self, word: str):
        try:
            with open(self._full_path) as file:
                if word in file.read():
                    return True
        except:
            return False
