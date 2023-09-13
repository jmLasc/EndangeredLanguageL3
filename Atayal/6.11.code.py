import string

def starts_with_number(line):
    line = line.strip()
    if len(line) > 0 and line[0].isdigit():
        return True
    return False

def copy_substring(line, end_chars):
    valid_start_chars = string.ascii_letters
    start_index = None
    for i, char in enumerate(line):
        if char in valid_start_chars:
            start_index = i
            break
    if start_index is None:
        return None
    i = start_index + 1
    while i < len(line):
        if line[i] in end_chars:
            # Check if the character following the end character is a Chinese character
            if i+1 < len(line) and line[i+1] >= '\u4e00' and line[i+1] <= '\u9fff':
                i += 1  # Include the Chinese character in the substring
            else:
                end_index = i
                substring = line[start_index:end_index + 1]
                return substring
        i += 1
    return None

def read_text_file(filename, stripped_output_file, end_chars):
    with open(filename, 'r', encoding='utf-8') as text_file:
        with open(stripped_output_file, 'w', encoding='utf-8') as stripped_output:
            next_line_starts_with_number = False
            for line in text_file:
                if next_line_starts_with_number:
                    stripped_output.write('\n')  # Write a new line before the next sentence
                    next_line_starts_with_number = False
                result = copy_substring(line, end_chars)
                if result is not None:
                    stripped_output.write(result)
                    next_line_starts_with_number = starts_with_number(line)

end_chars = ["。", "？", "！"]  # Specify the list of end characters

read_text_file('atayal_stripped6.9.txt', 'atayal_stripped6.11.txt', end_chars)
