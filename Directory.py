import os

class Directory:
    def __init__(self, name:str, parent: 'Directory'=None):
        self._name=name
        self._father_folder=parent
        self._contents=[]
        self._path=self.print_path()
        if self._father_folder is not None:
            self._father_folder.add_subfolder(self)

    @property
    def name(self):
        return self._name

    @property
    def path(self):
        return self._path

    @property
    def father_folder(self):
        return self._father_folder

    @property
    def contents(self):
        return self._contents


    def print_path(self):
        if self.father_folder==None:
            return os.getcwd()
        else:
            return f"{self.father_folder.print_path()}\{self.father_folder._name}"

    def add_subfolder(self, son_folder:'Directory'):
            if son_folder not in self.contents:
                self.contents.append(son_folder)
            if self.father_folder is not None:
                self.father_folder.add_subfolder(self)

    def add_file(self, file:'File'):
            if file not in self.contents:
                self.contents.append(file)


    def __getattr__(self, attr:str):
        try:
            for folder in self._contents:
                if folder._name == attr:
                    return folder
            return super().__getattribute__(attr)
        except AttributeError as e:
            raise e

    def __str__(self):
        return f"Folder {self.name} in {self.print_path()}"
    def __repr__(self):
        return f"Folder \"{self.name}\" in {self.print_path()}"

