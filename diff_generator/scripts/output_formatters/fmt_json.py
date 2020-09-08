import json


def format_as_json(diff, indent=4):
    return json.dumps(diff, indent=indent, sort_keys=True)
