import json
import yaml
import os


def load_file(file_path):
    file_loaders = {
        'json': json.load,
        'yaml': yaml.safe_load,
        'yml': yaml.safe_load,
    }

    file_extension = os.path.splitext(file_path)[1].strip('.')

    if file_extension not in file_loaders:
        raise ValueError('Unsupported file type.')

    with open(file_path) as file:
        return file_loaders[file_extension](file)
