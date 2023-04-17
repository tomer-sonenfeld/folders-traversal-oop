

import pytest
import builtins
from mockito import mock, when
from source.file import File


@pytest.fixture
def mocked_open():
    file_mock = mock()
    when(builtins).open('/root_dir/file1', 'r').thenReturn(file_mock)
    when(file_mock).__enter__().thenReturn(file_mock)
    when(file_mock).__exit__(...).thenReturn()
    return file_mock


def test_is_word_included__word_included(mocked_open, verify_mocks_were_stubbed):
    searched_word = "hello"
    when(mocked_open).read().thenReturn("hello world")
    tested_file = File('/root_dir/file1')
    assert tested_file.is_word_included(searched_word)


def test_is_word_included__word_not_included(mocked_open, verify_mocks_were_stubbed):
    searched_word = "hello"
    when(mocked_open).read().thenReturn("world")
    tested_file = File('/root_dir/file1')
    assert not tested_file.is_word_included(searched_word)


def test_is_word_included__unreadable_file(mocked_open, verify_mocks_were_stubbed):
    searched_word = "hello"
    when(mocked_open).read().thenRaise(UnicodeDecodeError('utf-8', b'hello', 0, 1, 'invalid start byte'))
    tested_file = File('/root_dir/file1')
    assert not tested_file.is_word_included(searched_word)




