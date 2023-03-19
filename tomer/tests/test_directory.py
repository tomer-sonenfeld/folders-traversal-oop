

import os
import pytest
from tomer import source

@pytest.fixture
def testing_folder_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "testing_folder")

def test_traverse(testing_folder_path):
    _dir = source.Directory(testing_folder_path)
    files_found = _dir.traverse()
    assert len(files_found) == 5
    expected_files = {os.path.join(testing_folder_path, "testing_file_include_word"),
                      os.path.join(testing_folder_path, "testing_file_exclude_word"),
                      os.path.join(testing_folder_path, "testing_sub_folder", "testing_file_include_word"),
                      os.path.join(testing_folder_path, "testing_sub_folder", "testing_file_exclude_word"),
                      os.path.join(testing_folder_path, "testing_file_unicode_error")
                      }
    assert set([f.path for f in files_found]) == expected_files


def test_files_with_content(testing_folder_path):
    word = "hello"
    _dir = source.Directory(testing_folder_path)
    files_found = _dir.traverse()
    files_found_with_word = _dir.files_with_content(word)
    assert len(files_found_with_word) == 2
    expected_files = {os.path.join(testing_folder_path, "testing_file_include_word"),
                      os.path.join(testing_folder_path, "testing_sub_folder", "testing_file_include_word")}
    assert set([f.path for f in files_found_with_word]) == expected_files