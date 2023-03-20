

import os
import pytest
from tomer.source.directory import Directory

@pytest.fixture
def testing_folder_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "testing_folder")

def test_traverse(testing_folder_path):
    _dir = Directory(testing_folder_path)
    files_found = _dir.traverse()
    expected_files = {os.path.join(testing_folder_path, "testing_file_include_word"),
                      os.path.join(testing_folder_path, "testing_file_exclude_word"),
                      os.path.join(testing_folder_path, "testing_sub_folder", "testing_file_include_word"),
                      os.path.join(testing_folder_path, "testing_sub_folder", "testing_file_exclude_word"),
                      os.path.join(testing_folder_path, "testing_file_unicode_error")
                      }
    assert set([_file.path for _file in files_found]) == expected_files


def test_files_with_content(testing_folder_path):
    word = "hello"
    _dir = Directory(testing_folder_path)
    files_found_with_word = _dir.files_with_content(word)
    expected_files = {os.path.join(testing_folder_path, "testing_file_include_word"),
                      os.path.join(testing_folder_path, "testing_sub_folder", "testing_file_include_word")}
    assert set([_file.path for _file in files_found_with_word]) == expected_files