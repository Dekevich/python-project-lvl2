from .file_loader import load_file
from .output_formatters.main import format_diff


def generate_formatted_diff(file_path_1, file_path_2, output_format):
    diff = generate_diff(
        load_file(file_path_1),
        load_file(file_path_2)
    )

    return format_diff(diff, output_format)


def generate_diff(data_before, data_after):
    removed = {key: {'status': 'removed', 'old_value': data_before[key]}
               for key in data_before.keys() - data_after.keys()}

    added = {key: {'status': 'added', 'new_value': data_after[key]}
             for key in data_after.keys() - data_before.keys()}

    updated = {}
    unmodified = {}

    for key in data_before.keys() & data_after.keys():
        val1 = data_before[key]
        val2 = data_after[key]

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
