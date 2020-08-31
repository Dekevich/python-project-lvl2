import argparse
import json


def generate_diff(file1, file2):
    with open(file1) as f:
        file1_data = json.load(f)

    with open(file2) as f:
        file2_data = json.load(f)

    result = []

    for key in file1_data.keys() - file2_data.keys():
        result.append(f'- {key}: {file1_data[key]}')

    for key in file2_data.keys() - file1_data.keys():
        result.append(f'+ {key}: {file2_data[key]}')

    for key in file1_data.keys() & file2_data.keys():
        file1_value = file1_data[key]
        file2_value = file2_data[key]

        if file1_value == file2_value:
            result.append(f'  {key}: {file1_value}')
        else:
            result.append(f'- {key}: {file1_value}')
            result.append(f'+ {key}: {file2_value}')

    return '{\n\t' + '\n\t'.join(result) + '\n}'


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
