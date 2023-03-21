

import os
import pytest
from mockito import mock, when, patch
from tomer.source.directory import Directory
from tomer.source.directory import File

def test_traverse(paths,mock_isdir,mock_isFile,mock_listdir):

    expected_files = {paths["testing_folder__testing_file_exclude_word"],
                      paths["testing_folder__testing_file_include_word"],
                      paths["testing_folder__testing_file_unicode_error"],
                      paths["testing_folder__testing_sub_folder__testing_file_exclude_word"],
                      paths["testing_folder__testing_sub_folder__testing_file_include_word"]}

    _dir = Directory(paths["testing_folder"])
    with patch('os.listdir', mock_listdir), patch('os.path.isfile', mock_isFile),\
    patch('os.path.isdir', mock_isdir):
                files_found = _dir.traverse()
    assert set([_file.path for _file in files_found]) == expected_files


def test_files_with_content(paths):

    word = "hello"
    _dir = Directory(paths["testing_folder"])

    testing_file_exclude_word = File(paths["testing_folder__testing_file_exclude_word"])
    testing_file_include_word = File(paths["testing_folder__testing_file_include_word"])

    when(_dir).traverse().thenReturn([testing_file_include_word, testing_file_exclude_word])

    when(testing_file_exclude_word).is_word_included(word).thenReturn(False)
    when(testing_file_include_word).is_word_included(word).thenReturn(True)

    expected_files = {paths["testing_folder__testing_file_include_word"]}

    files_found_with_word = _dir.files_with_content(word)

    assert set([_file.path for _file in files_found_with_word]) == expected_files
