import os
from tomer import source

def test_search_by_content():
    files_scanner = source.search.Search()
    test_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_folder")
    word="hello"
    files_found = files_scanner.search_by_content(test_folder_path,word)
    expected_files = {os.path.join(test_folder_path, "test_file_hello")}
    assert set([f for f in files_found]) == expected_files