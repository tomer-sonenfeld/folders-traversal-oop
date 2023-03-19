import os
from tomer import source
import pytest

@pytest.fixture
def word():
    return "hello"

@pytest.fixture
def files_scanner():
    return source.search.Search()

def test_search_by_content_existing_folder(word,files_scanner):
    testing_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testing_folder")
    files_found = files_scanner.search_by_content(testing_folder_path,word)
    expected_files = {os.path.join(testing_folder_path, "testing_file_include_word"),
                      os.path.join(testing_folder_path,"testing_sub_folder","testing_file_include_word")
                     }
    assert set([_file for _file in files_found]) == expected_files


def test_search_by_content_unexisting_folder(word,files_scanner):
    testing_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "unexisted_folder")
    with pytest.raises(source.exceptions.FolderNotFoundError):
        files_found = files_scanner.search_by_content(testing_folder_path, word)

def test_search_by_content_file_instead_of_folder(word,files_scanner):
    testing_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testing_folder", "testing_file_include_word")
    with pytest.raises(NotADirectoryError):
        files_found = files_scanner.search_by_content(testing_folder_path, word)



