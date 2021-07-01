import pytest
from jsonreader import *


def test_read_json_file_is_dict():
    filename = './test_run_results.json'
    output = read_jsonfile(filename)
    assert isinstance(output, dict)


