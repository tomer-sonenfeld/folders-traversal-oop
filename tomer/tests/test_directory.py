

import os
import pytest
from mockito import mock, when, patch
from tomer.source.directory import Directory

def test_traverse(paths,mock_isdir,mock_isFile,mock_listdir):

    expected_files = {paths["testing_folder__testing_file_exclude_word"],
                      paths["testing_folder__testing_file_include_word"],
                      paths["testing_folder__testing_file_unicode_error"],
                      paths["testing_folder__testing_sub_folder__testing_file_exclude_word"],
                      paths["testing_folder__testing_sub_folder__testing_file_include_word"]}

    _dir = Directory(paths["testing_folder"])
    with patch('os.listdir', mock_listdir):
        with patch('os.path.isfile', mock_isFile):
            with patch('os.path.isdir', mock_isdir):
                files_found = _dir.traverse()
    assert set([_file.path for _file in files_found]) == expected_files


def test_files_with_content(testing_folder_path):
    word = "hello"
    _dir = Directory(testing_folder_path)
    files_found_with_word = _dir.files_with_content(word)
    expected_files = {os.path.join(testing_folder_path, "testing_file_include_word"),
                      os.path.join(testing_folder_path, "testing_sub_folder", "testing_file_include_word")}
    assert set([_file.path for _file in files_found_with_word]) == expected_files
