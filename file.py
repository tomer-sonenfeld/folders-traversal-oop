import os


class File:

    def __init__(self, full_path: str):
        self._full_path = full_path

    def is_word_included(self, word: str):
        try:
            with open(self._full_path, 'r') as file:
                return word in file.read()
        except FileNotFoundError:
            print("File not found")
            return False
        except UnicodeDecodeError:
            print("Could not read file")
            return False

