import pytest

from diff_generator.scripts.gendiff import generate_formatted_diff

FLAT_JSON_1 = './tests/fixtures/flat_file_1.json'
FLAT_JSON_2 = './tests/fixtures/flat_file_2.json'
FLAT_YAML_1 = './tests/fixtures/flat_file_1.yml'
FLAT_YAML_2 = './tests/fixtures/flat_file_2.yml'
EXPECTED_FLAT = './tests/fixtures/expected_flat_json_like'

NESTED_JSON_1 = './tests/fixtures/nested_file_1.json'
NESTED_JSON_2 = './tests/fixtures/nested_file_2.json'
EXPECTED_JSON = './tests/fixtures/expected_nested_json'
EXPECTED_JSON_LIKE = './tests/fixtures/expected_nested_json_like'
EXPECTED_PLAIN = './tests/fixtures/expected_nested_plain'

test_param_names = [
    'file_path_1',
    'file_path_2',
    'output_format',
    'expected',
]

test_param_values = [
    (FLAT_JSON_1, FLAT_JSON_2, 'json-like', EXPECTED_FLAT),
    (FLAT_YAML_1, FLAT_YAML_2, 'json-like', EXPECTED_FLAT),
    (NESTED_JSON_1, NESTED_JSON_2, 'json-like', EXPECTED_JSON_LIKE),
    (NESTED_JSON_1, NESTED_JSON_2, 'json', EXPECTED_JSON),
    (NESTED_JSON_1, NESTED_JSON_2, 'plain', EXPECTED_PLAIN),
]

test_ids = [
    'flat JSON files, JSON-like output format',
    'flat YML files, JSON-like output format',
    'nested JSON files, JSON-like output format',
    'nested JSON files, JSON output format',
    'nested JSON files, plain output format',
]


@pytest.mark.parametrize(test_param_names, test_param_values, ids=test_ids)
def test_gendiff(file_path_1, file_path_2, output_format, expected):
    with open(expected) as f:
        expected_output = f.read()

    assert generate_formatted_diff(
        file_path_1, file_path_2, output_format
    ) == expected_output
