from training.dir import Dir
from mockito import when, mock, unstub
import pytest


@pytest.fixture
def get_test_dirs() -> dict:
    test_root = {"root": "root"}
    test_sub_root = ["fold0", "file0"]
    test_sub_root_paths = {x: test_root["root"] + "\\" + x for x in test_sub_root}
    test_sub_sub_root = ["fold1", "file1"]
    test_sub_sub_root_paths = {y: test_sub_root_paths[x] + "\\" + y for x in test_sub_root for y in test_sub_sub_root if
                               "file" not in x}
    test_dirs = {**test_root, **test_sub_root_paths, **test_sub_sub_root_paths}

    return test_dirs
