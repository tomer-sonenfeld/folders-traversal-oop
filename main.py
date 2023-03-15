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

    # Define the directory you want to traverse
    directory = os.getcwd()

    # Traverse the directory using os.walk()
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Do something with the file
            print(os.path.join(root, file))

    # result should include list of all paths that has the searched word..



