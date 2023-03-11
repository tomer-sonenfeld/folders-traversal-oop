import os

class File:

    def __init__(self,name,content="",father_folder=None):
        self._name=name
        self._content=content
        self._father_folder=father_folder
        self._path = self.printPath()
        if self._father_folder != None:
            self._father_folder.addFile(self)

    def printPath(self):
        if self._father_folder == None:
            return os.path.abspath('.')
        else:
            return f"{self._father_folder.printPath()}\{self._father_folder._name}"

    def printContent(self):
        print(self._content)

    def getContent(self):
        return self._content

    def __str__(self):
        return f"File {self._name} in {self.printPath()}"

    def __repr__(self):
        return f"File \"{self._name}\" in {self.printPath()}"


