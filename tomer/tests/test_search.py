import os
import pytest
from tomer.source.search import Search
from tomer.source.exceptions import NonExistingDirectory
from tomer.source.directory import Directory
from mockito import when


@pytest.fixture
def files_scanner():
    return Search()

def test_search_by_content__unexisted_path(paths,files_scanner):
    word="hello"
    unexisted_path = paths["testing_folder\\unexisted_path"]
    when(os.path).exists(unexisted_path).thenReturn(False)
    with pytest.raises(NonExistingDirectory):
        files_scanner.search_by_content(unexisted_path,word)

def test_search_by_content__path_is_file(paths,files_scanner):
    word="hello"
    tested_file_path = paths["testing_folder\\testing_file"]
    when(os.path).exists(tested_file_path).thenReturn(True)
    when(os.path).isdir(tested_file_path).thenReturn(False)
    expected_files=tested_file_path
    files_found=files_scanner.search_by_content(tested_file_path,word)
    assert files_found == expected_files


def test_search_by_content__existing_folder(paths,files_scanner):
    word = "hello"
    tested_folder_path = paths["testing_folder"]
    when(os.path).exists(tested_folder_path).thenReturn(True)
    when(os.path).isdir(tested_folder_path).thenReturn(True)
    _dir = Directory(tested_folder_path)
    when(Directory).files_with_content(word).thenReturn(paths["testing_folder\\testing_file_include_word"])
    files_found = files_scanner.search_by_content(tested_folder_path,word)
    expected_files = paths["testing_folder\\testing_file_include_word"]
    assert files_found == expected_files

def test_search_by_content__existing_folder_with_sub_folder(paths,files_scanner):
    word = "hello"
    tested_folder_path = paths["testing_folder"]
    when(os.path).exists(tested_folder_path).thenReturn(True)
    when(os.path).isdir(tested_folder_path).thenReturn(True)
    _dir = Directory(tested_folder_path)
    when(Directory).files_with_content(word).thenReturn([paths["testing_folder\\testing_file_include_word"],paths["testing_folder\\testing_sub_folder\\testing_file_include_word"]])
    files_found = files_scanner.search_by_content(tested_folder_path,word)
    expected_files = [paths["testing_folder\\testing_file_include_word"],paths["testing_folder\\testing_sub_folder\\testing_file_include_word"]]
    assert files_found == expected_files



