import numpy as np

def save_file_contents_to_file(file_contents, file):
    file_contents = convert_all_values_to_string(file_contents)
    max_lengths = get_max_lengths(file_contents)
    write_contents_to_file(file_contents, max_lengths, file)

def convert_all_values_to_string(file_contents):
    for key, values in file_contents.items():
        strings = [str(value) for value in values]
        file_contents[key] = strings
    return file_contents

def get_max_lengths(file_contents):
    max_lengths = [get_max_length(key, values)
                for key, values in file_contents.items()]
    return max_lengths

def get_max_length(key, values):
    value_lengths = [len(value) for value in values]
    max_length = max(len(key), max(value_lengths))
    return max_length

def write_contents_to_file(file_contents, max_lengths, file):
    write_column_headers(file_contents, max_lengths, file)
    write_column_values(file_contents, max_lengths, file)

def write_column_headers(file_contents, max_lengths, file):
    headers = file_contents.keys()
    write_row(headers, max_lengths, file)

def write_column_values(file_contents, max_lengths, file):
    file_contents = np.array([np.array(column)
                              for column in file_contents.values()])
    file_contents = np.transpose(file_contents)
    for row in file_contents:
        write_row(row, max_lengths, file)

def write_row(row, max_lengths, file):
    for value, max_length in zip(row, max_lengths):
        spacing = (max_length + 2 - len(value)) * " "
        file.writelines(f"{value}{spacing}")
    file.writelines("\n")
