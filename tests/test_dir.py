import mockito
import pytest
from training.dir import Dir
import os.path
from mockito import when, mock, unstub
import training.file_path as file_path


def test_path_property_no_parent():
    when(os.path).join("", "root").thenReturn('root')
    when(os.path).isdir('root').thenReturn(True)
    fullpath = 'root'
    curr_dir = Dir(fullpath)
    assert fullpath == curr_dir.path


def test_path_property_with_parent():
    when(os.path).join("", "root").thenReturn('root')
    when(os.path).isdir('root').thenReturn(True)
    fullpath = 'root'
    parent_dir = Dir(fullpath)
    when(os.path).join("root", "fold0").thenReturn('root\\fold0')
    when(os.path).isdir('root\\fold0').thenReturn(True)
    child_dir = Dir("fold0", parent_dir)
    assert "fold0" == child_dir.path


def test_fullpath_property_no_parent():
    when(os.path).join("", "root").thenReturn('root')
    fullpath = 'root'
    curr_dir = Dir(fullpath)
    assert fullpath == curr_dir.fullpath


def test_fullpath_property_with_parent():
    when(os.path).join("", "root").thenReturn('root')
    fullpath = 'root'
    parent_dir = Dir(fullpath)
    when(os.path).join("root", "fold0").thenReturn('root\\fold0')
    child_dir = Dir("fold0", parent_dir)
    assert 'root\\fold0' == child_dir.fullpath


def test_parent_property_no_parent():
    when(os.path).join("", "root").thenReturn('root')
    fullpath = 'root'
    curr_dir = Dir(fullpath)
    assert curr_dir.parent is None


def test_parent_property_with_parent():
    when(os.path).join("", "root").thenReturn('root')
    fullpath = 'root'
    parent_dir = Dir(fullpath)
    when(os.path).join("root", "fold0").thenReturn('root\\fold0')
    child_dir = Dir("fold0", parent_dir)
    assert "fold0" == child_dir.path


def test_match_files_os_listdir_empty():
    when(os.path).join("", "root").thenReturn('root')
    when(os.path).isdir('root').thenReturn(True)
    when(os).listdir('root').thenReturn([])

    fullpath = 'root'
    root_dir = Dir(fullpath)
    result = root_dir.match_files("list_dir_empty")
    assert set(result) == set()


def test_match_files_os_listdir_not_empty():
    when(os.path).join("", "root").thenReturn('root')
    when(os.path).join('root', "file0").thenReturn("root\\file0")
    when(os.path).isdir('root').thenReturn(True)
    when(os.path).isdir("root\\file0").thenReturn(False)
    when(os).listdir('root').thenReturn(["file0"])
    fullpath = 'root'
    root_dir = Dir(fullpath)
    result = root_dir.match_files("list_dir_not_empty")
    assert set(result) == set()

def test_match_files_file_path_from_path_none():
    when(os.path).join("", "root").thenReturn('root')
    when(os.path).join('root', "file0").thenReturn("root\\file0")
    when(os.path).isdir('root').thenReturn(True)
    when(os.path).isdir("root\\file0").thenReturn(False)
    when(os).listdir('root').thenReturn(["file0"])
    when(file_path.File).from_path("root\\file0").thenReturn(None)
    fullpath = 'root'
    root_dir = Dir(fullpath)
    result = root_dir.match_files("list_dir_not_empty")
    assert set(result) == set()

def test_match_files_file_path_from_path_not_none():
    when(os.path).join("", "root").thenReturn('root')
    when(os.path).join('root', "file0").thenReturn("root\\file0")
    when(os.path).isdir('root').thenReturn(True)
    when(os.path).isdir("root\\file0").thenReturn(False)
    when(os).listdir('root').thenReturn(["file0"])
    mock_file0 = mock()
    when(file_path.File).from_path("root\\file0").thenReturn(mock_file0)
    when(mock_file0).word_match('in_directory').thenReturn(False)
    fullpath = 'root'
    root_dir = Dir(fullpath)
    result = root_dir.match_files("list_dir_not_empty")
    assert set(result) == set()

def test_match_files_file_only_in_root_directory():
    when(os.path).join("", "root").thenReturn('root')
    when(os.path).join('root', "file0").thenReturn("root\\file0")
    when(os.path).isdir('root').thenReturn(True)
    when(os.path).isdir("root\\file0").thenReturn(False)

    mock_file0 = mock()
    when(file_path.File).from_path("root\\file0").thenReturn(mock_file0)
    when(mock_file0).word_match('in_directory').thenReturn(True)
    fullpath = 'root'
    root_dir = Dir(fullpath)
    result = root_dir.match_files("in_directory")
    assert set(result) == {"root\\file0"}


def test_match_files_file_in_sub_root_directory():
    when(os.path).join("", "root").thenReturn('root')
    when(os.path).join("root\\fold0", "file1").thenReturn("root\\fold0\\file1")
    when(os.path).isdir('root').thenReturn(True)
    when(os.path).isdir('root\\fold0').thenReturn(True)
    when(os).listdir('root').thenReturn(["fold0"])
    when(os).listdir('root\\fold0').thenReturn(["file1"])

    when(os.path).join('root\\fold0', "file1").thenReturn("root\\fold0\\file1")
    when(os.path).isdir("root\\fold0\\file1").thenReturn(False)
    when(os).listdir('root\\fold0').thenReturn(["file1"])

    mock_file1 = mock()
    when(file_path.File).from_path("root\\fold0\\file1").thenReturn(mock_file1)
    when(mock_file1).word_match('in_directory').thenReturn(True)
    fullpath = 'root'
    root_dir = Dir(fullpath)
    result = root_dir.match_files("in_directory")
    assert set(result) == {"root\\fold0\\file1"}


def test_match_files_2_files_in_directory_and_sub_root():
    when(os.path).join("", "root").thenReturn('root')
    when(os.path).join('root', "file0").thenReturn("root\\file0")
    when(os.path).join("root\\fold0", "file1").thenReturn("root\\fold0\\file1")

    when(os.path).isdir('root').thenReturn(True)
    when(os.path).isdir('root\\fold0').thenReturn(True)
    when(os.path).isdir("root\\file0").thenReturn(False)
    when(os.path).isdir("root\\fold0\\file1").thenReturn(False)

    when(os).listdir('root').thenReturn(["fold0", "file0"])
    when(os).listdir('root\\fold0').thenReturn(["file1"])

    mock_file = mock()
    when(file_path.File).from_path("root\\file0").thenReturn(mock_file)
    when(mock_file).word_match('in_directory').thenReturn(True)

    when(file_path.File).from_path("root\\fold0\\file1").thenReturn(mock_file)
    when(mock_file).word_match('in_directory').thenReturn(True)

    fullpath = 'root'
    root_dir = Dir(fullpath)
    result = root_dir.match_files("in_directory")
    assert set(result) == {"root\\file0", "root\\fold0\\file1"}