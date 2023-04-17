import os
from mockito import when
from source.file import File
from source.directory import Directory


def test_list_of_files_in_dirs__file_with_word_found(verify_mocks_were_stubbed):
    when(os.path).isdir('/root_dir').thenReturn(True)
    tested_folder = Directory('/root_dir')
    expected_list_of_files = ['/root_dir/file1']
    searched_word = "hello"

    when(os).listdir('/root_dir').thenReturn(["file1"])
    when(os.path).join('/root_dir', 'file1').thenReturn('/root_dir/file1')
    when(os.path).isdir('/root_dir/file1').thenReturn(False)
    when(os.path).isfile('/root_dir/file1').thenReturn(True)
    when(File).is_word_included(searched_word).thenReturn(True)

    result = tested_folder.list_of_files_in_dirs(searched_word)

    assert result == expected_list_of_files


def test_list_of_files_in_dirs__file_without_word(verify_mocks_were_stubbed):
    when(os.path).isdir('/root_dir').thenReturn(True)
    tested_folder = Directory('/root_dir')
    expected_list_of_files = []
    searched_word = "hello"

    when(os).listdir('/root_dir').thenReturn(["file1"])
    when(os.path).join('/root_dir', 'file1').thenReturn('/root_dir/file1')
    when(os.path).isdir('/root_dir/file1').thenReturn(False)
    when(os.path).isfile('/root_dir/file1').thenReturn(True)
    when(File).is_word_included(searched_word).thenReturn(False)

    result = tested_folder.list_of_files_in_dirs(searched_word)

    assert result == expected_list_of_files


