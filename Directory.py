import os

class Directory:

    def __init__(self,name,father_folder=None):
        self._name=name
        self._father_folder=father_folder
        self._contents=[]
        self._path=self.printPath()
        if self._father_folder!=None:
            self._father_folder.addSubfolder(self)


    def printPath(self):
        if self._father_folder==None:
            return os.path.abspath('.')
        else:
            return f"{self._father_folder.printPath()}\{self._father_folder._name}"

    def addSubfolder(self,son_folder):
            if son_folder not in self._contents:
                self._contents.append(son_folder)
            if self._father_folder != None:
                self._father_folder.addSubfolder(self)

    def addFile(self,file):
            if file not in self._contents:
                self._contents.append(file)


    def __getattr__(self, attr):
        try:
            for folder in self._contents:
                if folder._name == attr:
                    return folder
            return super().__getattribute__(attr)
        except AttributeError as e:
            raise e

    def __str__(self):
        return f"Folder {self._name} in {self.printPath()}"
    def __repr__(self):
        return f"Folder \"{self._name}\" in {self.printPath()}"

    def getContents(self):
        return self._contents
