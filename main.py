import os
import Directory


def files_that_contains_word_in_dir(dir_path:str, word:str):
    res = []
    directory = Directory.Directory(dir_path)
    return directory.lookup_str_in_files(word)


if __name__ == '__main__':
    #Probably have to adapt the paths to Linux to make it work there.
    print(files_that_contains_word_in_dir("C:/test_root/","Hello World"))

