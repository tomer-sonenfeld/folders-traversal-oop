import os


class File:

    def __init__(self, full_path: str):
        self._full_path = full_path

    def is_word_included(self, word: str):
        try:
            with open(self._full_path) as file:
                return word in file.read()
        except:
            print("File not opened")
