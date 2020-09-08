from .fmt_json import format_as_json
from .fmt_plain import format_as_plain_text
from .fmt_json_like import format_as_json_like


def format_diff(diff, output_format):
    formatters = {
        'plain': format_as_plain_text,
        'json': format_as_json,
        'json-like': format_as_json_like,
    }

    return formatters[output_format](diff)
