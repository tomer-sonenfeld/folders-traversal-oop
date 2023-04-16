import os
import directory
import pytest
from mockito import when
from unittest.mock import patch, mock_open


def test_not_directory_exception_caught():
    when(os.path).isdir("/root_test/").thenReturn(False)
    with pytest.raises(Exception):
        directory.Directory("/root_test/")


@patch("builtins.open", mock_open(read_data="Foo"))
def test_found_file_with_word():
    file_path = os.path.join("/root_test/", "file")
    expected_output = [file_path]

    when(os.path).isdir("/root_test/").thenReturn(True)
    when(os).listdir("/root_test/").thenReturn(["file"])

    when(os.path).isfile(file_path).thenReturn(True)
    when(os.path).isdir(file_path).thenReturn(False)

    test_dir = directory.Directory("/root_test/")
    assert test_dir.lookup_str_in_files("Foo") == expected_output


@patch("builtins.open", mock_open(read_data="Foo"))
def test_not_found_file_with_word():
    expected_output = []
    file_path = os.path.join("/root_test/", "file")

    when(os.path).isdir("/root_test/").thenReturn(True)
    when(os).listdir("/root_test/").thenReturn(["file"])

    when(os.path).isfile(file_path).thenReturn(True)
    when(os.path).isdir(file_path).thenReturn(False)

    test_dir = directory.Directory("/root_test/")
    assert test_dir.lookup_str_in_files("Bar") == expected_output


@patch("builtins.open", mock_open(read_data="Foo"))
def test_found_nested_file_with_word():
    nested_folder_path = os.path.join("/root_test/", "nested_folder")
    file_path = os.path.join(nested_folder_path, "file")
    expected_output = [file_path]

    when(os.path).isdir("/root_test/").thenReturn(True)
    when(os).listdir("/root_test/").thenReturn(["nested_folder"])

    when(os.path).isfile(nested_folder_path).thenReturn(False)
    when(os.path).isdir(nested_folder_path).thenReturn(True)
    when(os).listdir(nested_folder_path).thenReturn(["file"])

    when(os.path).isfile(file_path).thenReturn(True)
    when(os.path).isdir(file_path).thenReturn(False)

    test_dir = directory.Directory("/root_test/")
    assert test_dir.lookup_str_in_files("Foo") == expected_output


@patch("builtins.open", mock_open(read_data="Foo"))
def test_found_multiple_files_with_word():
    nested_folder_path = os.path.join("/root_test/", "nested_folder")
    file_path = os.path.join("/root_test/", "file")
    nested_file_path = os.path.join(nested_folder_path, "nested_file")
    expected_output = {file_path, nested_file_path}

    when(os.path).isdir("/root_test/").thenReturn(True)
    when(os).listdir("/root_test/").thenReturn(["nested_folder", "file"])

    when(os.path).isfile(nested_folder_path).thenReturn(False)
    when(os.path).isdir(nested_folder_path).thenReturn(True)

    when(os.path).isfile(file_path).thenReturn(True)
    when(os.path).isdir(file_path).thenReturn(False)

    when(os).listdir(nested_folder_path).thenReturn(["nested_file"])
    when(os.path).isfile(nested_file_path).thenReturn(True)
    when(os.path).isdir(nested_file_path).thenReturn(False)

    test_dir = directory.Directory("/root_test/")
    assert set(test_dir.lookup_str_in_files("Foo")) == expected_output