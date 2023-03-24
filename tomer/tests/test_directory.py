

import os
from mockito import when
from tomer.source.directory import Directory
from tomer.source.directory import File



def test_traverse__file_found(paths):

    expected_files = {paths["testing_folder\\testing_file"]}
    testing_folder_path = paths["testing_folder"]
    when(os.path).isdir(testing_folder_path).thenReturn(True)
    _dir = Directory(testing_folder_path)
    when(os).listdir(testing_folder_path).thenReturn(["testing_file"])
    when(os.path).isfile(paths["testing_folder\\testing_file"]).thenReturn(True)
    files_found = _dir.traverse()
    assert set([_file.path for _file in files_found]) == expected_files


def test_traverse__nested_file_found(paths):

    expected_files = {paths["testing_folder\\testing_file"],
                      paths["testing_folder\\testing_sub_folder\\testing_file"]}
    testing_folder_path = paths["testing_folder"]
    testing_sub_folder_path = paths["testing_folder\\testing_sub_folder"]
    when(os.path).isdir(testing_folder_path).thenReturn(True)
    _dir = Directory(testing_folder_path)
    when(os).listdir(testing_folder_path).thenReturn(["testing_file","testing_sub_folder"])
    when(os).listdir(testing_sub_folder_path).thenReturn(["testing_file"])
    when(os.path).isdir(paths["testing_folder\\testing_sub_folder"]).thenReturn(True)
    when(os.path).isfile(testing_sub_folder_path).thenReturn(False)
    when(os.path).isfile(paths["testing_folder\\testing_file"]).thenReturn(True)
    when(os.path).isfile(paths["testing_folder\\testing_sub_folder\\testing_file"]).thenReturn(True)
    files_found = _dir.traverse()


    assert set([_file.path for _file in files_found]) == expected_files



def test_files_with_content__file_with_word(paths):

    word = "hello"
    testing_folder_path = paths["testing_folder"]
    when(os.path).isdir(testing_folder_path).thenReturn(True)
    _dir = Directory(paths["testing_folder"])
    testing_file_include_word = File(paths["testing_folder\\testing_file_include_word"])
    when(_dir).traverse().thenReturn([testing_file_include_word])
    when(testing_file_include_word).is_word_included(word).thenReturn(True)
    expected_files = {paths["testing_folder\\testing_file_include_word"]}
    files_found_with_word = _dir.files_with_content(word)
    assert set([_file.path for _file in files_found_with_word]) == expected_files

def test_files_with_content__file_without_word(paths):

    word = "hello"
    testing_folder_path = paths["testing_folder"]
    testing_file_exclude_word = File(paths["testing_folder\\testing_file_exclude_word"])
    when(os.path).isdir(testing_folder_path).thenReturn(True)
    _dir = Directory(paths["testing_folder"])
    when(_dir).traverse().thenReturn([testing_file_exclude_word])
    when(testing_file_exclude_word).is_word_included(word).thenReturn(False)
    expected_files = set()
    files_found_with_word = _dir.files_with_content(word)
    assert set([_file.path for _file in files_found_with_word]) == expected_files

def test_files_with_content__file_with_word_and_without_word(paths):

    word = "hello"
    testing_folder_path = paths["testing_folder"]
    testing_file_include_word = File(paths["testing_folder\\testing_file_include_word"])
    testing_file_exclude_word = File(paths["testing_folder\\testing_file_exclude_word"])
    when(os.path).isdir(testing_folder_path).thenReturn(True)
    _dir = Directory(paths["testing_folder"])
    when(_dir).traverse().thenReturn([testing_file_include_word,testing_file_exclude_word])
    when(testing_file_include_word).is_word_included(word).thenReturn(True)
    when(testing_file_exclude_word).is_word_included(word).thenReturn(False)
    expected_files = {paths["testing_folder\\testing_file_include_word"]}
    files_found_with_word = _dir.files_with_content(word)
    assert set([_file.path for _file in files_found_with_word]) == expected_files

def test_files_with_content__file_with_word_and_without_word_and_nested_file_with_word(paths):

    word = "hello"
    testing_folder_path = paths["testing_folder"]
    testing_file_include_word = File(paths["testing_folder\\testing_file_include_word"])
    testing_file_exclude_word = File(paths["testing_folder\\testing_file_exclude_word"])
    testing_file_include_word_nested = File(paths["testing_folder\\testing_sub_folder\\testing_file_include_word"])
    when(os.path).isdir(testing_folder_path).thenReturn(True)
    _dir = Directory(paths["testing_folder"])
    when(_dir).traverse().thenReturn([testing_file_include_word,testing_file_exclude_word,testing_file_include_word_nested])
    when(testing_file_include_word).is_word_included(word).thenReturn(True)
    when(testing_file_exclude_word).is_word_included(word).thenReturn(False)
    when(testing_file_include_word_nested).is_word_included(word).thenReturn(True)
    expected_files = {paths["testing_folder\\testing_file_include_word"],paths["testing_folder\\testing_sub_folder\\testing_file_include_word"]}
    files_found_with_word = _dir.files_with_content(word)
    assert set([_file.path for _file in files_found_with_word]) == expected_files