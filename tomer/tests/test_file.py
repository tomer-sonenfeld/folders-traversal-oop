import os
from tomer import source

def test_is_word_included_word_included():
    word="hello"
    test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_folder", "test_file_hello")
    _file = source.File(test_file_path)
    assert _file.is_word_included(word)

def test_is_word_included_word_not_included():
    word="hello"
    test_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_folder", "test_file_no_hello")
    _file = source.File(test_file_path)
    assert not _file.is_word_included(word)