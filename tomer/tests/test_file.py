

import pytest
from mockito import when, mock
from tomer.source.file import File
import builtins


def test_is_word_included__word_included(paths):
    word="hello"
    testing_file_path = paths["testing_folder\\testing_file_include_word"]
    file_mock = mock()
    _file = File(testing_file_path)
    when(builtins).open(testing_file_path,'r').thenReturn(file_mock)
    when(file_mock).read().thenReturn("hello world")
    when(file_mock).__enter__().thenReturn(file_mock)
    when(file_mock).__exit__().thenReturn(None)
    assert _file.is_word_included(word)


def test_is_word_included__word_not_included(paths):
    word="hello"
    testing_file_path = paths["testing_folder\\testing_file_exclude_word"]
    file_mock = mock()
    _file = File(testing_file_path)
    when(builtins).open(testing_file_path,'r').thenReturn(file_mock)
    when(file_mock).read().thenReturn("world")
    when(file_mock).__enter__().thenReturn(file_mock)
    when(file_mock).__exit__().thenReturn(None)
    assert not _file.is_word_included(word)

def test_is_word_included__file_not_found(paths):
    word="hello"
    testing_file_path = paths["testing_folder\\unexisted_path"]
    _file = File(testing_file_path)
    when(builtins).open(testing_file_path,'r').thenRaise(FileNotFoundError)
    with pytest.raises(FileNotFoundError):
        _file.is_word_included(word)


def test_is_word_included__unreadable_file(paths):
    word="hello"
    testing_file_path = paths["testing_folder\\testing_file_unicode_error"]
    file_mock = mock()
    _file = File(testing_file_path)
    when(builtins).open(testing_file_path,'r').thenReturn(file_mock)
    when(file_mock).__enter__().thenReturn(file_mock)
    when(file_mock).__exit__().thenReturn(None)
    when(file_mock).read().thenRaise(UnicodeDecodeError("",bytes(65),0,0,""))
    assert not _file.is_word_included(word)

def test_is_word_included__empty_file(paths):
    word="hello"
    testing_file_path = paths["testing_folder\\testing_file"]
    file_mock = mock()
    _file = File(testing_file_path)
    when(builtins).open(testing_file_path,'r').thenReturn(file_mock)
    when(file_mock).read().thenReturn("")
    when(file_mock).__enter__().thenReturn(file_mock)
    when(file_mock).__exit__().thenReturn(None)
    assert not _file.is_word_included(word)

