import pytest
from training.dir import Dir
import os.path
from mockito import when, mock, unstub
from training.file_path import File
from training.tests.fixtures import test_dirs

# test_dirs = get_test_dirs()


def test_path_property_no_parent(test_dirs):
    when(os.path).join("", "root").thenReturn(test_dirs["root"])
    fullpath = test_dirs["root"]
    curr_dir = Dir(fullpath)
    assert fullpath == curr_dir.path


def test_path_property_with_parent(test_dirs):
    when(os.path).join("", "root").thenReturn(test_dirs["root"])
    fullpath = test_dirs["root"]
    parent_dir = Dir(fullpath)
    when(os.path).join("root", "fold0").thenReturn(test_dirs["fold0"])
    child_dir = Dir("fold0", parent_dir)
    assert "fold0" == child_dir.path


def test_fullpath_property_no_parent(test_dirs):
    when(os.path).join("", "root").thenReturn(test_dirs["root"])
    fullpath = test_dirs["root"]
    curr_dir = Dir(fullpath)
    assert fullpath == curr_dir.fullpath


def test_fullpath_property_with_parent(test_dirs):
    when(os.path).join("", "root").thenReturn(test_dirs["root"])
    fullpath = test_dirs["root"]
    parent_dir = Dir(fullpath)
    when(os.path).join("root", "fold0").thenReturn(test_dirs["fold0"])
    child_dir = Dir("fold0", parent_dir)
    assert test_dirs["fold0"] == child_dir.fullpath


def test_parent_property_no_parent(test_dirs):
    when(os.path).join("", "root").thenReturn(test_dirs["root"])
    fullpath = test_dirs["root"]
    curr_dir = Dir(fullpath)
    assert curr_dir.parent is None


def test_parent_property_with_parent(test_dirs):
    when(os.path).join("", "root").thenReturn(test_dirs["root"])
    fullpath = test_dirs["root"]
    parent_dir = Dir(fullpath)
    when(os.path).join("root", "fold0").thenReturn(test_dirs["fold0"])
    child_dir = Dir("fold0", parent_dir)
    assert "fold0" == child_dir.path

# stuff to mock
# File.check_path
# word_match
# mock os.listdir
"""
def test_match_files_in_directory(test_dirs):
    when(os.path).join("", "root").thenReturn(test_dirs["root"])
    when(os.path).join(test_dirs["root"], "file0").thenReturn(test_dirs["file0"])
    when(os.path).join(test_dirs["root"], "fold0").thenReturn(test_dirs["fold0"])
    when(os.path).join(test_dirs["fold0"], "file1").thenReturn(test_dirs["file1"])
    when(os.path).join(test_dirs["fold0"], "fold1").thenReturn(test_dirs["fold1"])

    when(os.path).isdir(test_dirs["root"]).thenReturn(True)
    when(os.path).isdir(test_dirs["fold0"]).thenReturn(True)
    when(os.path).isdir(test_dirs["file0"]).thenReturn(False)
    when(os.path).isdir(test_dirs["fold1"]).thenReturn(True)
    when(os.path).isdir(test_dirs["file1"]).thenReturn(False)

    when(os).listdir(test_dirs["root"]).thenReturn(["file0", "fold0"])
    when(os).listdir(test_dirs["fold0"]).thenReturn(["file1", "fold1"])
    when(os).listdir(test_dirs["fold1"]).thenReturn([])

    when(File).check_path(test_dirs["file0"]).thenReturn(True)
    when(File).check_path(test_dirs["file1"]).thenReturn(True)

    file_mock = mock(File)

    file0 = mock({'_fullpath': test_dirs["file0"]})
    file1 = mock({'_fullpath': test_dirs["file1"]})
    # breakpoint()
    when(file_mock).__init__(test_dirs["file0"]).thenReturn(file0)
    when(file_mock).__init__(test_dirs["file1"]).thenReturn(file1)

    when(file0).word_match("in_directory").thenReturn(True)
    when(file1).word_match("in_directory").thenReturn(False)

    fullpath = test_dirs["root"]
    root_dir = Dir(fullpath)
    result = root_dir.match_files("in_directory")
    #assert set(result) == {test_dirs["file0"]}
    assert True
"""
