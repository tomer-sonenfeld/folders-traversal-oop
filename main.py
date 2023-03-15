from Directory import Directory
from File import File
import os
from Search import Search

def files_that_contains(folder: 'Directory', word:str):
    files=[]
    for item in folder.contents:
        if isinstance(item,File):
            if word in item.content:
                files.append(item)
        elif isinstance(item,Directory):
            files.extend(files_that_contains(item, word))
    return files

    def Search(self):
        return Search()


if __name__ == "__main__":

    files_scanner = Search()
    print(files_scanner.search_by_content(r"C:\Users\tomer\PycharmProjects\Training\testFolder","hello"))






