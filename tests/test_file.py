import pytest
import builtins
from mockito import when, mock, unstub
from training.file import File
import os.path


def test_from_path_not_file_expected_null():
    bad_file_path = "fake/veryfake"
    when(os.path).isfile(bad_file_path).thenReturn(False)
    f = File.from_path(bad_file_path)
    assert f is None


def test_from_path_good_file_path_expected_file_object():
    good_file_path = "root/file0"
    when(os.path).isfile(good_file_path).thenReturn(True)
    assert File.from_path(good_file_path) is not None


def test_word_match_open_file_fails():
    bad_fullpath = "root/bad_file"
    test_file = File(bad_fullpath)
    word = "test fail"
    try:
        test_file.word_match(word)
    except:
        pass
    else:
        assert False, "FileNotFoundError has not been outputed"


def test_word_match_word_found_in_file():
    filepath = "root/file0"
    test_file = File(filepath)
    mock_file = mock()
    when(builtins).open(filepath, "r").thenReturn(mock_file)
    when(mock_file).__enter__().thenReturn(mock_file)
    when(mock_file).__exit__().thenReturn()
    test_file_string = "string file representation has test keyword"
    when(mock_file).read().thenReturn(test_file_string)
    word = "test"
    assert test_file.word_match(word)


def test_word_match_word_not_found_in_file():
    filepath = "root/file0"
    test_file = File(filepath)
    mock_file = mock()
    when(builtins).open(filepath, "r").thenReturn(mock_file)
    when(mock_file).__enter__().thenReturn(mock_file)
    when(mock_file).__exit__().thenReturn()
    test_file_string = "string file representation has test keyword"
    when(mock_file).read().thenReturn(test_file_string)
    word = "nothing"
    assert not test_file.word_match(word)

