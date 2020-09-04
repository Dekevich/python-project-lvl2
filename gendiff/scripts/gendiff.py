def generate_diff(file1_data, file2_data):
    result = []

    for key in sorted(file1_data.keys() | file2_data.keys()):
        if key in file1_data and key not in file2_data:
            result.append(f'- {key}: {file1_data[key]}')
        elif key in file2_data and key not in file1_data:
            result.append(f'+ {key}: {file2_data[key]}')
        elif file1_data[key] == file2_data[key]:
            result.append(f'  {key}: {file1_data[key]}')
        else:
            result.append(f'- {key}: {file1_data[key]}')
            result.append(f'+ {key}: {file2_data[key]}')

    return '{\n  ' + '\n  '.join(result) + '\n}'
