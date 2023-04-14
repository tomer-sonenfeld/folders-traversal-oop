import pytest
from training.dir import Dir
import os.path
from mockito import when, mock
import training.file_path as file_path


# from path - file/not file
# word_match - open fails, open success - word found, word not found
