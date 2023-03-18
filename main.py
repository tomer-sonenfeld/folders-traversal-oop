import directory


def files_that_contains_word_in_dir(dir_path:str, word:str):
    _dir = directory.Directory(dir_path)
    return _dir.lookup_str_in_files(word)


if __name__ == '__main__':
    # Probably have to adapt the paths to Linux to make it work there.
    print(files_that_contains_word_in_dir("D:/root_test/", "Hello World"))
    new_dir = directory.Directory("D:/root_test/")
    print(new_dir.lookup_str_in_files("Hello World"))
    print("end")
