import re

def remove_brackets(input_file, output_file):
    with open(input_file, 'r') as file:
        data = file.read()

    # Remove brackets and their contents
    data = re.sub(r'\[.*?\]', '', data)
    data = re.sub(r'\(.*?\)', '', data)
    data = re.sub(r'\（.*?\）', '', data)

# Remove incomplete brackets and everything until the next line
    data = re.sub(r'\[.*', '', data)
    data = re.sub(r'\(.*', '', data)

    with open(output_file, 'w') as file:
        file.write(data)


# def add_newlines(input_file, output_file):
#     with open(input_file, 'r') as file:
#         data = file.readlines()

#     # Process each line
#     formatted_data = []
#     for line in data:
#         line = line.strip()  # Remove leading/trailing whitespace

#         # Check if line has multiple sentences
#         if re.search(r'[\u4e00-\u9fff]|[A-Za-z\'\"]|。|？|！', line):
#             line = re.sub(r'(。|？|！)(?=[^。？！\u4e00-\u9fff])', r'\1\n', line)

#         # Check if line ends with ? and is followed by Romanized characters, ', or "
#         if re.search(r'\?(?=[\u4e00-\u9fffA-Za-z\'"])$', line):
#             line += '\n'

#         formatted_data.append(line)

#     with open(output_file, 'w') as file:
#         file.write('\n'.join(formatted_data))


# Example usage
remove_brackets("amis_stripped_final.txt", "amis_stripped_no_bracket.txt")

# add_newlines("sakizaya_stripped_no_bracket.txt", "sakizaya_stripped_no_bracket_final.txt")