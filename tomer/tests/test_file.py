

import pytest
import builtins
from mockito import when, mock, verifyStubbedInvocationsAreUsed, unstub
from tomer.source.file import File

@pytest.mark.parametrize("mocked_open",['/root_dir/file1'], indirect=True)
def test_is_word_included__word_included(mocked_open):
    word="hello"
    when(mocked_open).read().thenReturn("hello world")
    _file = File('/root_dir/file1')
    assert _file.is_word_included(word)
    verifyStubbedInvocationsAreUsed()
    unstub();

@pytest.mark.parametrize("mocked_open",['/root_dir/file1'], indirect=True)
def test_is_word_included__word_not_included(mocked_open):
    word="hello"
    when(mocked_open).read().thenReturn("world")
    _file = File('/root_dir/file1')
    assert not _file.is_word_included(word)
    verifyStubbedInvocationsAreUsed()
    unstub();


def test_is_word_included__file_not_found():
    word="hello"
    when(builtins).open('/root_dir/file1', 'r').thenRaise(FileNotFoundError)
    _file = File('/root_dir/file1')
    with pytest.raises(FileNotFoundError):
        _file.is_word_included(word)
    verifyStubbedInvocationsAreUsed()
    unstub();


@pytest.mark.parametrize("mocked_open",['/root_dir/file1'], indirect=True)
def test_is_word_included__unreadable_file(mocked_open):
    word="hello"
    when(mocked_open).read().thenReturn("")
    _file = File('/root_dir/file1')
    assert not _file.is_word_included(word)
    verifyStubbedInvocationsAreUsed()
    unstub();

@pytest.mark.parametrize("mocked_open",['/root_dir/file1'], indirect=True)
def test_is_word_included__empty_file(paths,mocked_open):
    word="hello"
    when(mocked_open).read().thenReturn("")
    _file = File('/root_dir/file1')
    assert not _file.is_word_included(word)
    verifyStubbedInvocationsAreUsed()
    unstub();


