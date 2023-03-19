import os
from tomer import source

def test_traverse():
    test_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_folder")
    _dir = source.Directory(test_folder_path)
    files_found = _dir.traverse()
    assert len(files_found) == 2
    expected_files = {os.path.join(test_folder_path,"test_file_hello"),
           os.path.join(test_folder_path,"test_file_no_hello")}
    assert set([f.path for f in files_found]) == expected_files

def test_files_with_content():
    word = "hello"
    test_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_folder")
    _dir = source.Directory(test_folder_path)
    files_found = _dir.traverse()
    files_found_with_word = _dir.files_with_content(word)
    assert len(files_found_with_word) == 1
    expected_files = {os.path.join(test_folder_path, "test_file_hello")}
    assert set([f.path for f in files_found_with_word]) == expected_files