import argparse

from .scripts.gendiff import generate_diff
from .scripts.file_loader import load_file


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    file1_data = load_file(args.first_file)
    file2_data = load_file(args.second_file)

    print(generate_diff(file1_data, file2_data))


if __name__ == '__main__':
    main()
