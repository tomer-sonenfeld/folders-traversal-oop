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

    def __getattr__(self, attr):
        try:
            for folder in self._contents:
                if folder._name == attr:
                    return folder
            return super().__getattribute__(attr)
        except AttributeError as e:
            raise e

#C:\Users\tomer\PycharmProjects\Training\x\y\z
#1.enter y as a content of x
#2.create the path as abspath\x