

import pytest
import os
from mockito import when, mock,patch

@pytest.fixture
def paths() -> dict:

    paths = dict()
    paths["testing_folder"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testing_folder")
    paths["testing_folder__testing_file_exclude_word"] = \
        os.path.join(paths["testing_folder"], "testing_file_exclude_word")
    paths["testing_folder__testing_file_include_word"] = \
        os.path.join(paths["testing_folder"], "testing_file_include_word")
    paths["testing_folder__testing_file_unicode_error"] = \
        os.path.join(paths["testing_folder"], "testing_file_unicode_error")
    paths["testing_folder__testing_sub_folder"] = \
        os.path.join(paths["testing_folder"], "testing_sub_folder")
    paths["testing_folder__testing_sub_folder__testing_file_exclude_word"] = \
        os.path.join(paths["testing_folder__testing_sub_folder"], "testing_file_exclude_word")
    paths["testing_folder__testing_sub_folder__testing_file_include_word"] = \
        os.path.join(paths["testing_folder__testing_sub_folder"], "testing_file_include_word")

    return paths

@pytest.fixture()
def mock_listdir(paths):
    mock_listdir = mock()

    when(mock_listdir).__call__(paths["testing_folder"]).thenReturn(["testing_file_include_word",
                                                                 "testing_file_exclude_word",
                                                                 "testing_file_unicode_error",
                                                                 "testing_sub_folder"
                                                                     ])

    when(mock_listdir).__call__(paths["testing_folder__testing_sub_folder"]).thenReturn(
                                                                 ["testing_file_include_word",
                                                                 "testing_file_exclude_word"
                                                                 ])


    return mock_listdir

@pytest.fixture()
def mock_isFile(paths):
    mock_isFile = mock()

    when(mock_isFile).__call__(paths["testing_folder"]).thenReturn(False)
    when(mock_isFile).__call__(paths["testing_folder__testing_sub_folder"]).thenReturn(False)
    when(mock_isFile).__call__(paths["testing_folder__testing_file_exclude_word"]).thenReturn(True)
    when(mock_isFile).__call__(paths["testing_folder__testing_file_include_word"]).thenReturn(True)
    when(mock_isFile).__call__(paths["testing_folder__testing_file_unicode_error"]).thenReturn(True)
    when(mock_isFile).__call__(paths["testing_folder__testing_sub_folder__testing_file_exclude_word"]).thenReturn(True)
    when(mock_isFile).__call__(paths["testing_folder__testing_sub_folder__testing_file_include_word"]).thenReturn(True)

    return mock_isFile

@pytest.fixture()
def mock_isdir(paths):
    mock_isdir = mock()

    when(mock_isdir).__call__(paths["testing_folder"]).thenReturn(True)
    when(mock_isdir).__call__(paths["testing_folder__testing_sub_folder"]).thenReturn(True)
    when(mock_isdir).__call__(paths["testing_folder__testing_file_exclude_word"]).thenReturn(False)
    when(mock_isdir).__call__(paths["testing_folder__testing_file_include_word"]).thenReturn(False)
    when(mock_isdir).__call__(paths["testing_folder__testing_file_unicode_error"]).thenReturn(False)
    when(mock_isdir).__call__(paths["testing_folder__testing_sub_folder__testing_file_exclude_word"]).thenReturn(False)
    when(mock_isdir).__call__(paths["testing_folder__testing_sub_folder__testing_file_include_word"]).thenReturn(False)

    return mock_isdir