import os
import pytest

from tomer.source.file import File
from tomer.source.search import Search
from tomer.source.exceptions import NonExistingPathError
from tomer.source.directory import Directory
from mockito import when,unstub,verifyStubbedInvocationsAreUsed


def test_search_by_content__non_existing_path():
    word="hello"
    tested= Search()

    when(os.path).exists('/root_dir/file1').thenReturn(False)

    with pytest.raises(NonExistingPathError):
        tested.search_by_content('/root_dir/file1',word)

    verifyStubbedInvocationsAreUsed()

    unstub()

def test_search_by_content__path_is_file_with_word():
    expected={'/root_dir/file1'}
    word="hello"
    tested= Search()

    when(os.path).exists('/root_dir/file1').thenReturn(True)
    when(os.path).isdir('/root_dir/file1').thenReturn(False)
    when(os.path).isfile('/root_dir/file1').thenReturn(True)
    when(File).is_word_included(word).thenReturn(True)

    result=tested.search_by_content('/root_dir/file1',word)

    assert result == expected

    verifyStubbedInvocationsAreUsed()
    unstub()

def test_search_by_content__path_is_file_without_word():
    expected=set()
    word="hello"
    tested= Search()

    when(os.path).exists('/root_dir/file1').thenReturn(True)
    when(os.path).isdir('/root_dir/file1').thenReturn(False)
    when(os.path).isfile('/root_dir/file1').thenReturn(True)
    when(File).is_word_included(word).thenReturn(False)

    result=tested.search_by_content('/root_dir/file1',word)

    assert result == expected

    verifyStubbedInvocationsAreUsed()
    unstub()


def test_search_by_content__existing_folder():
    expected = '/root_dir/file1'
    word = "hello"
    tested= Search()

    when(os.path).exists('/root_dir').thenReturn(True)
    when(os.path).isdir('/root_dir').thenReturn(True)
    when(Directory).files_with_content(word).thenReturn('/root_dir/file1')

    result = tested.search_by_content('/root_dir',word)

    assert result == expected

    verifyStubbedInvocationsAreUsed()
    unstub()


def test_search_by_content__existing_folder_with_sub_folder():
    expected = ['/root_dir/file1','/root_dir/sub_dir/file2']
    word = "hello"
    tested= Search()

    when(os.path).exists('/root_dir').thenReturn(True)
    when(os.path).isdir('/root_dir').thenReturn(True)
    when(Directory).files_with_content(word).thenReturn(['/root_dir/file1','/root_dir/sub_dir/file2'])

    result = tested.search_by_content('/root_dir',word)

    assert result == expected

    verifyStubbedInvocationsAreUsed()
    unstub()


