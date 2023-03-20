

import os
import pytest
from tomer.source.file import File


def test_is_word_included__word_included():
    word="hello"
    testing_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testing_folder", "testing_file_include_word")
    _file = File(testing_file_path)
    assert _file.is_word_included(word)

def test_is_word_included__word_not_included():
    word = "hello"
    testing_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testing_folder", "testing_file_exclude_word")
    _file = File(testing_file_path)
    assert not _file.is_word_included(word)

def test_unreadable_file():
    word = "hello"
    testing_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testing_folder", "testing_file_unicode_error")
    _file = File(testing_file_path)
    with pytest.raises(UnicodeDecodeError):
        with open(_file.path, 'r', encoding='ascii') as _file_opened:
            content = _file_opened.read()

