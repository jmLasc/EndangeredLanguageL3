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
    substring = line[start_index:].strip()
    return substring


def read_text_file(filename, stripped_output_file):
    with open(filename, 'r', encoding='utf-8') as text_file:
        with open(stripped_output_file, 'w', encoding='utf-8') as stripped_output:
            should_log = False
            current_line = ''
            for line in text_file:
                line = line.strip()
                if line and line[0].isdigit():
                    should_log = True
                    if current_line:
                        stripped_output.write(current_line + '\n')
                    current_line = line
                elif should_log:
                    if line:
                        current_line += ' ' + line
                    else:
                        stripped_output.write(current_line + '\n')
                        current_line = ''
            if current_line:
                stripped_output.write(current_line + '\n')


read_text_file('atayal_stripped.txt', 'atayal_stripped6.9.txt')
