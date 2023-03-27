

import os
from mockito import when, mock
from tomer.source.directory import Directory
from tomer.source.file import File

def test_traverse__file_found(verify_mocks_were_stubbed):
    expected_file_path = {'/root_dir/file1'}

    when(os).listdir('/root_dir').thenReturn(["file1"])
    when(os.path).join('/root_dir', 'file1').thenReturn('/root_dir/file1')
    when(os.path).isfile('/root_dir/file1').thenReturn(True)

    tested = Directory('/root_dir')
    result = tested.traverse()

    assert set([_file.path for _file in result]) == expected_file_path


def test_traverse__nested_files_found(verify_mocks_were_stubbed):
    expected_files_paths = {'/root_dir/file1', '/root_dir/sub_dir/file2'}

    when(os).listdir('/root_dir').thenReturn(["file1", "sub_dir"])
    when(os.path).join('/root_dir', 'file1').thenReturn('/root_dir/file1')
    when(os.path).isfile('/root_dir/file1').thenReturn(True)
    when(os.path).join('/root_dir', 'sub_dir').thenReturn('/root_dir/sub_dir')
    when(os.path).isdir('/root_dir/sub_dir').thenReturn(True)
    when(os.path).isfile('/root_dir/sub_dir').thenReturn(False)
    when(os).listdir('/root_dir/sub_dir').thenReturn(["file2"])
    when(os.path).join('/root_dir/sub_dir', 'file2').thenReturn('/root_dir/sub_dir/file2')
    when(os.path).isfile('/root_dir/sub_dir/file2').thenReturn(True)

    tested = Directory('/root_dir')
    result = tested.traverse()

    assert set([_file.path for _file in result]) == expected_files_paths


def test_files_with_content__file_with_word(verify_mocks_were_stubbed):
    expected_file_path = {'/root_dir/file1'}
    searched_word = "hello"
    tested_folder = Directory('/root_dir')
    tested_file = mock({'path': '/root_dir/file1'}, spec=File)

    when(tested_folder).traverse().thenReturn([tested_file])
    when(tested_file).is_word_included(searched_word).thenReturn(True)

    result = tested_folder.files_with_content(searched_word)

    assert set([_file.path for _file in result]) == expected_file_path


def test_files_with_content__file_without_word(verify_mocks_were_stubbed):
    expected_files_paths = set()
    searched_word = "hello"
    tested_folder = Directory('/root_dir')
    tested_file = mock({'path': '/root_dir/file1'}, spec=File)

    when(tested_folder).traverse().thenReturn([tested_file])
    when(tested_file).is_word_included(searched_word).thenReturn(False)

    result = tested_folder.files_with_content(searched_word)

    assert set([_file.path for _file in result]) == expected_files_paths
