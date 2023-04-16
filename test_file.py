import os
import file
import pytest
from mockito import when
from unittest.mock import patch, mock_open


def test_not_directory_exception_caught():
    when(os.path).isfile("/file").thenReturn(False)
    with pytest.raises(Exception):
        file.File("/file")


@patch("builtins.open", mock_open(read_data="Foo"))
def test_file_with_word():
    file_path = os.path.join("/root_test/", "file")
    when(os.path).isfile(file_path).thenReturn(True)
    test_file = file.File(file_path)
    assert test_file.lookup_str_in_file("Foo")


@patch("builtins.open", mock_open(read_data="Foo"))
def test_not_found_file_with_word():
    file_path = os.path.join("/root_test/", "file")
    when(os.path).isfile(file_path).thenReturn(True)
    test_file = file.File(file_path)
    assert not test_file.lookup_str_in_file("Bar")
