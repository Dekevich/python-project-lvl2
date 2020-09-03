import argparse
import json


def generate_diff(file_path_1, file_path_2):
    with open(file_path_1) as file:
        file1_data = json.load(file)

    with open(file_path_2) as file:
        file2_data = json.load(file)

    result = []

    for key in sorted(file1_data.keys() | file2_data.keys()):
        if key in file1_data and key not in file2_data:
            result.append(f'- {key}: {file1_data[key]}')
        elif key in file2_data and key not in file1_data:
            result.append(f'+ {key}: {file2_data[key]}')
        elif file1_data[key] == file2_data[key]:
            result.append(f'  {key}: {file1_data[key]}')
        else:
            result.append(f'- {key}: {file1_data[key]}')
            result.append(f'+ {key}: {file2_data[key]}')

    return '{\n  ' + '\n  '.join(result) + '\n}'


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
