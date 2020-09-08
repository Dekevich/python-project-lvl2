def format_as_plain_text(diff):
    full_key_path = []

    def inner(diff):
        result = []
        for key, key_data in diff.items():
            full_key_path.append(key)
            status = key_data.get('status')
            if not status:
                result.extend(inner(key_data))
            elif status != 'unmodified':

                result.append(
                    generate_output_line(key_data, '.'.join(full_key_path))
                )
            full_key_path.pop()
        return result

    return '\n'.join(sorted(inner(diff)))


def generate_output_line(key_data, key_path):
    line_templates = {
        'removed': "Property '{path}' was removed",
        'added': "Property '{path}' was added with value: {new_value}",
        'updated': "Property '{path}' was updated. From {old_value} to {new_value}",  # noqa: E501
    }

    return line_templates[key_data['status']].format(
        **reformat_key_data(key_data), path=key_path
    )


def reformat_key_data(key_data):
    formatters = {
        str: lambda x: f"'{x}'",
        list: lambda x: '[complex value]',
        dict: lambda x: '[complex value]',
        'default': lambda x: x,
    }

    result = {}
    for key, value in key_data.items():
        formatter = formatters.get(type(value), formatters['default'])
        result[key] = formatter(value)

    return result
