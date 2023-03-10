import os

class Directory:

    def __init__(self, name, father_folder=None):
        self.name=name
        self.contents = []
        self.father_folder=father_folder
        if self.father_folder!=None:
            self.path=self.father_folder.printPath() + "\\" + self.name
            self.father_folder.add_content(self)
        else:
            self.path = os.path.abspath(".") + "\\" + self.name



    def printPath(self):
        if self.father_folder==None:
            return os.path.abspath(".") + "\\" + self.name
        else:
            return self.father_folder.printPath() + "\\" + self.name


    def add_content(self,son_folder):
        if son_folder not in self.contents:
            self.contents.append(son_folder)
        if self.father_folder!=None:
            self.father_folder.add_content(self)

    def __getattr__(self, name):
        try:
            return super().__getattr__(name)
        except AttributeError:
            if name in self.__dict__:
                return self.__dict__[name]
            for sub_folder in self.contents:
                if sub_folder.name==name:
                    return sub_folder

