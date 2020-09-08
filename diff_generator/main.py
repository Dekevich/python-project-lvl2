import argparse
import sys

from diff_generator.gendiff import generate_formatted_diff


def parse_args(args):
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        choices=['plain', 'json', 'json-like'],
                        default='json-like',
                        help='set format of output')

    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])
    diff = generate_formatted_diff(
        args.first_file, args.second_file, args.format
    )

    print(diff)


if __name__ == '__main__':
    main()
