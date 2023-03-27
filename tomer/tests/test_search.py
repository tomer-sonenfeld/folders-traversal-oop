import os
import pytest
from tomer.source.file import File
from tomer.source.search import Search
from tomer.source.exceptions import NonExistingPathError
from tomer.source.directory import Directory
from mockito import when, verify


def test_search_by_content__non_existing_path(verify_mocks_were_stubbed):
    searched_word = "hello"

    when(os.path).exists('/root_dir/file1').thenReturn(False)

    tested = Search()

    with pytest.raises(NonExistingPathError):
        tested.search_by_content('/root_dir/file1', searched_word)


def test_search_by_content__path_is_file(verify_mocks_were_stubbed):
    searched_word = "hello"

    when(os.path).exists('/root_dir/file1').thenReturn(True)
    when(os.path).isdir('/root_dir/file1').thenReturn(False)
    when(os.path).isfile('/root_dir/file1').thenReturn(True)
    when(File).is_word_included(searched_word).thenReturn(None)

    tested = Search()
    tested.search_by_content('/root_dir/file1', searched_word)

    verify(File, times=1).is_word_included(searched_word)


def test_search_by_content__path_is_folder(verify_mocks_were_stubbed):
    searched_word = "hello"

    when(os.path).exists('/root_dir').thenReturn(True)
    when(os.path).isdir('/root_dir').thenReturn(True)
    when(Directory).files_with_content(searched_word).thenReturn(None)

    tested = Search()
    tested.search_by_content('/root_dir', searched_word)

    verify(Directory, times=1).files_with_content(searched_word)
