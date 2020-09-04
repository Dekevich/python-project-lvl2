import pytest

from gendiff.scripts.file_loader import load_file
from gendiff.scripts.gendiff import generate_diff

flat_files = [
    ('./tests/fixtures/flat_file_1.json', './tests/fixtures/flat_file_2.json'),
    ('./tests/fixtures/flat_file_1.yml', './tests/fixtures/flat_file_2.yml'),
]


@pytest.mark.parametrize(
    ['file_path_1', 'file_path_2'], flat_files, ids=['json', 'yaml']
)
def test_flat_files(file_path_1, file_path_2):
    file1_data = load_file(file_path_1)
    file2_data = load_file(file_path_2)

    with open('./tests/fixtures/expected') as f:
        expected_output = f.read()

    assert generate_diff(file1_data, file2_data) == expected_output
