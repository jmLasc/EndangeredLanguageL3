import string

def copy_substring(line):
    valid_start_chars = string.ascii_letters 
    start_index = None
    for i, char in enumerate(line):
        if char in valid_start_chars:
            start_index = i
            break
    if start_index is None:
        return None
    end_index = line.find('\n', start_index)
    if end_index != -1:
        substring = line[start_index:end_index]
        return substring
    elif start_index != len(line):
        substring = line[start_index:]
        return substring
    return None


def read_text_file(filename, stripped_output_file):
    with open(filename, 'r', encoding='utf-8') as text_file:
        with open(stripped_output_file, 'w', encoding='utf-8') as stripped_output:
            for line in text_file:
                result = copy_substring(line)
                if result is not None:
                    stripped_output.write(result + '\n')

read_text_file('atayal_stripped.txt', 'atayal_stripped6.8.txt')
