from Directory import Directory
import os

class Search:

    def search_by_content(self, path:str, word:str):
        if os.path.exists(path):
            dir = Directory(path)
            files_list = dir.traverse()
            return dir.files_with_content(word)
        else:
            return "Path does'nt exists"