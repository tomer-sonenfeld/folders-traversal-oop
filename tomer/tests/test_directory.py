import os
from tomer import source

def test_traverse():
    _dir = source.Directory(os.path.join(os.path.dirname(os.path.abspath(__file__)),"directory_to_traverse"))
    files_found = _dir.traverse()
    assert len(files_found) == 2
    assert files_found.