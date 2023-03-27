

import pytest
import builtins
from mockito import mock, when
from tomer.source.file import File


@pytest.fixture
def mocked_open(request):
    testing_file_path = request.param
    file_mock = mock()
    when(builtins).open(testing_file_path, 'r').thenReturn(file_mock)
    when(file_mock).__enter__().thenReturn(file_mock)
    when(file_mock).__exit__(None, None, None).thenReturn()
    return file_mock


@pytest.mark.parametrize("mocked_open", ['/root_dir/file1'], indirect=True)
def test_is_word_included__word_included(mocked_open, teardown):
    searched_word = "hello"
    when(mocked_open).read().thenReturn("hello world")

    tested = File('/root_dir/file1')

    assert tested.is_word_included(searched_word)


@pytest.mark.parametrize("mocked_open", ['/root_dir/file1'], indirect=True)
def test_is_word_included__word_not_included(mocked_open, teardown):
    searched_word = "hello"
    when(mocked_open).read().thenReturn("world")

    tested = File('/root_dir/file1')

    assert not tested.is_word_included(searched_word)


@pytest.mark.parametrize("mocked_open", ['/root_dir/file1'], indirect=True)
def test_is_word_included__unreadable_file(mocked_open, teardown):
    searched_word = "hello"
    when(mocked_open).read().thenRaise(UnicodeDecodeError('utf-8', b'hello', 0, 1, 'invalid start byte'))

    tested = File('/root_dir/file1')

    assert not tested.is_word_included(searched_word)
