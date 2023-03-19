

import os
import pytest
from tomer import source

@pytest.fixture
def word():
    return "hello"

def test_is_word_included_word_included(word):
    test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testing_folder", "testing_file_include_word")
    _file = source.File(test_file_path)
    assert _file.is_word_included(word)

def test_is_word_included_word_not_included(word):
    test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testing_folder", "testing_file_exclude_word")
    _file = source.File(test_file_path)
    assert not _file.is_word_included(word)

def test_is_word_included_unreadable_file(word):
    test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testing_folder", "testing_file_unicode_error")
    _file = source.File(test_file_path)
    with pytest.raises(UnicodeDecodeError):
        with open(_file.path, 'r', encoding='ascii') as _file_opened:
            content = _file_opened.read()

