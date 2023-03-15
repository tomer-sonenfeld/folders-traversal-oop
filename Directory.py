import os

class Directory:
    def __init__(self, path:str):
        self._path=path
        self._my_files=[]

    def traverse(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                self.my_files.append(os.path.join(root, file))
        return self.my_files

    def files_with_content(self,word:str):
        files_with_word=[]
        for file in self.my_files:
            if os.path.isfile(file) and file.endswith('.txt'):
                with open(file, 'r') as file_opened:
                    file_contents = file_opened.read()
                    if word in file_contents:
                        files_with_word.append(file)
        return files_with_word



    @property
    def name(self):
        return self._name

    @property
    def my_files(self):
        return self._my_files

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

