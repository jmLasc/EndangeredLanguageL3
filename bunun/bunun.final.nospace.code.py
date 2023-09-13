def add_newline_chinese_punctuation(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        modified_line = ''
        ignore_bracket = False  # Flag to ignore punctuation within brackets
        for i, char in enumerate(line):
            modified_line += char
            if char == '[' or char == '(':
                ignore_bracket = True
            elif char == ']' or char == ')':
                ignore_bracket = False
            elif char in '。？！' and not ignore_bracket and i < len(line) - 1 and line[i + 1] != '\n':
                modified_line += '\n'
        modified_lines.append(modified_line)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

    print("Output file created: " + output_file)


input_file = "bunun_stripped_final.txt"
output_file = "bunun_stripped_final_nospace.txt"
add_newline_chinese_punctuation(input_file, output_file)
