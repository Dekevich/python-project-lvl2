from gendiff.scripts.gendiff import generate_diff


def test_flat_json_diff():
    file1_path = './tests/fixtures/flat_file_1.json'
    file2_path = './tests/fixtures/flat_file_2.json'

    with open('./tests/fixtures/expected') as f:
        expected_output = f.read()

    assert generate_diff(file1_path, file2_path) == expected_output
