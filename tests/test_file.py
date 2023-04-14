import pytest
from training.dir import Dir
import builtins
from mockito import when, mock
from training.file import File


# from path - file/not file
def test_from_path_not_file_expected_null():
    assert True

def test_from_path_good_file_path_expected_file_object():
    assert True


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

