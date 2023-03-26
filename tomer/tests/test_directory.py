

import os
from mockito import when, verifyStubbedInvocationsAreUsed, unstub
from tomer.source.directory import Directory
from tomer.source.directory import File


def test_traverse__file_found():
    expected = {os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file1")}
    when(os).listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir")).thenReturn(["file1"])
    when(os.path).isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file1")).thenReturn(True)
    tested = Directory(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir"))
    result = tested.traverse()
    assert set([_file.path for _file in result]) == expected
    verifyStubbedInvocationsAreUsed();
    unstub();


def test_traverse__nested_files_found():
    expected = {os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file1"),
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "sub_dir", "file2")}
    when(os).listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir")).thenReturn(["file1", "sub_dir"])
    when(os.path).isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file1")).thenReturn(True)
    when(os.path).isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "sub_dir")).thenReturn(False)
    when(os.path).isdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "sub_dir")).thenReturn(True)
    when(os).listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "sub_dir")).thenReturn(["file2"])
    when(os.path).isfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "sub_dir", "file2")).thenReturn(True)
    tested = Directory(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir"))
    result = tested.traverse()
    assert set([_file.path for _file in result]) == expected
    verifyStubbedInvocationsAreUsed();
    unstub();


def test_files_with_content__file_with_word():
    expected = {os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file1")}
    word = "hello"
    tested_folder = Directory(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file1"))
    tested_file = File(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file1"))
    when(tested_folder).traverse().thenReturn([tested_file])
    when(tested_file).is_word_included(word).thenReturn(True)
    result = tested_folder.files_with_content(word)
    assert set([_file.path for _file in result]) == expected
    verifyStubbedInvocationsAreUsed();
    unstub();


def test_files_with_content__file_without_word():
    expected = set()
    word = "hello"
    tested_folder = Directory(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file1"))
    tested_file = File(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file1"))
    when(tested_folder).traverse().thenReturn([tested_file])
    when(tested_file).is_word_included(word).thenReturn(False)
    result = tested_folder.files_with_content(word)
    assert set([_file.path for _file in result]) == expected
    verifyStubbedInvocationsAreUsed();
    unstub();


def test_files_with_content__file_with_word_and_without_word():
    expected = {os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file1")}
    word = "hello"
    tested_folder = Directory(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file1"))
    tested_file_include_word = File(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file1"))
    tested_file_exclude_word = File(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file2"))
    when(tested_folder).traverse().thenReturn([tested_file_include_word,tested_file_exclude_word])
    when(tested_file_include_word).is_word_included(word).thenReturn(True)
    when(tested_file_exclude_word).is_word_included(word).thenReturn(False)
    result = tested_folder.files_with_content(word)
    assert set([_file.path for _file in result]) == expected
    verifyStubbedInvocationsAreUsed();
    unstub();


def test_files_with_content__file_with_word_and_without_word_and_nested_file_with_word():
    expected = {os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file1"),
                os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "sub_dir", "file2")}
    word = "hello"
    tested_folder = Directory(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file1"))
    tested_file_include_word = File(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file1"))
    tested_file_exclude_word = File(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "file2"))
    tested_file_nested_include_word = File(os.path.join(os.path.dirname(os.path.abspath(__file__)), "root_dir", "sub_dir", "file2"))
    when(tested_folder).traverse().thenReturn([tested_file_include_word,tested_file_exclude_word,tested_file_nested_include_word])
    when(tested_file_include_word).is_word_included(word).thenReturn(True)
    when(tested_file_exclude_word).is_word_included(word).thenReturn(False)
    when(tested_file_nested_include_word).is_word_included(word).thenReturn(True)
    result = tested_folder.files_with_content(word)
    assert set([_file.path for _file in result]) == expected
    verifyStubbedInvocationsAreUsed();
    unstub();