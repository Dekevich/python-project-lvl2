from .file_loader import load_file
from .output_formatters.main import format_diff


def generate_formatted_diff(file_path_1, file_path_2, output_format):
    diff = generate_diff(
        load_file(file_path_1),
        load_file(file_path_2)
    )

    return format_diff(diff, output_format)


def generate_diff(dict1, dict2):
    removed = {key: {'status': 'removed', 'old_value': dict1[key]}
               for key in dict1.keys() - dict2.keys()}

    added = {key: {'status': 'added', 'new_value': dict2[key]}
             for key in dict2.keys() - dict1.keys()}

    updated = {}
    unmodified = {}

    for key in dict1.keys() & dict2.keys():
        val1 = dict1[key]
        val2 = dict2[key]

        if val1 == val2:
            unmodified[key] = {'status': 'unmodified', 'old_value': val1}
        elif isinstance(val1, dict) and isinstance(val2, dict):
            updated[key] = generate_diff(val1, val2)
        else:
            updated[key] = {
                'status': 'updated',
                'old_value': val1,
                'new_value': val2
            }

    return {**removed, **added, **updated, **unmodified}
