import builtins

import pytest
import os

from mockito import when, mock


@pytest.fixture
def paths() -> dict:

    paths = dict()
    paths["testing_folder"] = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testing_folder")
    paths["testing_folder\\testing_file_exclude_word"] = \
        os.path.join(paths["testing_folder"], "testing_file_exclude_word")
    paths["testing_folder\\testing_file_include_word"] = \
        os.path.join(paths["testing_folder"], "testing_file_include_word")
    paths["testing_folder\\testing_file_unicode_error"] = \
        os.path.join(paths["testing_folder"], "testing_file_unicode_error")
    paths["testing_folder\\testing_sub_folder"] = \
        os.path.join(paths["testing_folder"], "testing_sub_folder")
    paths["testing_folder\\testing_sub_folder\\testing_file_exclude_word"] = \
        os.path.join(paths["testing_folder\\testing_sub_folder"], "testing_file_exclude_word")
    paths["testing_folder\\testing_sub_folder\\testing_file_include_word"] = \
        os.path.join(paths["testing_folder\\testing_sub_folder"], "testing_file_include_word")
    paths["testing_folder\\testing_file"] = \
        os.path.join(paths["testing_folder"], "testing_file")
    paths["testing_folder\\testing_sub_folder\\testing_file"] = \
        os.path.join(paths["testing_folder\\testing_sub_folder"], "testing_file")
    paths["testing_folder\\unexisted_path"] = \
        os.path.join(paths["testing_folder"], "unexisted_path")

    return paths


@pytest.fixture
def mocked_open(request):
    testing_file_path = request.param
    file_mock = mock()
    when(builtins).open(testing_file_path, 'r').thenReturn(file_mock)
    when(file_mock).__enter__().thenReturn(file_mock)
    when(file_mock).__exit__(None, None, None).thenReturn()
    return file_mock

@pytest.fixture
def my_fixture(request):
    arg_value = request.param
    # do something with the argument value
    result = arg_value * 2
    return result