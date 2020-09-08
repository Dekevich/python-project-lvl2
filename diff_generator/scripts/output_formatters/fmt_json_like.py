import json
import re


def format_as_json_like(diff, indent=2):
    def inner(diff):
        result = {}
        for key, key_data in sorted(diff.items()):
            status = key_data.get('status')
            if not status:
                result[f'{key}'] = inner(key_data)
            else:
                result.update(
                    {fkey: fvalue for fkey, fvalue
                     in format_key(key, key_data, status)}
                )

        return result

    output = json.dumps(inner(diff), indent=4)
    # return output
    return re.sub('[,"]', '', output)


def format_key(key, key_data, status):
    format_modifiers = {
        'added': [('+', 'new_value')],
        'removed': [('-', 'old_value')],
        'unmodified': [(' ', 'old_value')],
        'updated': [('-', 'old_value'), ('+', 'new_value')]
    }

    return [(f'{prefix} {key}', key_data.get(value))
            for prefix, value in format_modifiers[status]]
