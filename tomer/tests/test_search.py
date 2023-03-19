import os
from tomer import source
import pytest

def test_search_by_content_existing_folder():
    files_scanner = source.search.Search()
    test_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_folder")
    word="hello"
    files_found = files_scanner.search_by_content(test_folder_path,word)
    expected_files = {os.path.join(test_folder_path, "test_file_hello")}
    assert set([f for f in files_found]) == expected_files


def test_search_by_content_unexisting_folder():
    files_scanner = source.search.Search()
    test_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "unexisted_folder")
    word = "hello"
    with pytest.raises(source.exceptions.FolderNotFoundError):
        files_found = files_scanner.search_by_content(test_folder_path, word)

def test_search_by_content_file_instead_of_folder():
    files_scanner = source.search.Search()
    test_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_folder","test_file_hello")
    word = "hello"
    with pytest.raises(NotADirectoryError):
        files_found = files_scanner.search_by_content(test_folder_path, word)



