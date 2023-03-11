import os

class File:
    def __init__(self,name:str,content:str,father_folder:'Directory'=None):
        self._name=name
        self._content=content
        self._father_folder=father_folder
        self._path = self.print_path()
        if self.father_folder != None:
            self.father_folder.add_file(self)
        with open(name, 'w') as f:
            f.write(self.content)

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
    def content(self):
        return self._content

    def print_path(self):
        if self._father_folder == None:
            return os.getcwd()
        else:
            return f"{self.father_folder.print_path()}\{self.father_folder._name}"

    def print_content(self):
        print(self._content)


    def __str__(self):
        return f"File {self.name} in {self.print_path()}"

    def __repr__(self):
        return f"File \"{self.name}\" in {self.print_path()}"


