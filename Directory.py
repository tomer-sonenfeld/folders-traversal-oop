import os
import ntpath

class FailedToCreateDirectory(Exception):
    pass
class FailedToReadFromFile(Exception):
    pass

class Directory(object):
    def __init__(self,path:str,father_directory:'Directory'=None):
        self._path = path
        self._father_directory = father_directory
        self._subdirectories = []
        self._files = []
        self.scan_folder()

    def scan_folder(self):
        for item in os.listdir(self._path):
           if os.path.isdir(f"{self._path}{item}"):
               try:
                x = Directory(f"{self._path}{item}/",self)
                self._subdirectories.append(x)
               except:
                  raise FailedToCreateDirectory(f"{self._path}{item}/")
           else:
               self._files.append(f"{self._path}{item}")

    def lookup_str_in_files(self,word:str):
        res = []
        for file in self._files:
            try:
                f = open(file,"r")
                if word in f:
                    path, file_name = ntpath.split(file)
                    res.append(file_name)
            except:
                raise FailedToReadFromFile(f"{self._path}{file}")
        for dir in self._subdirectories:
            res.extend(dir.lookup_str_in_files(word))
        return res

