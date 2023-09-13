import re

def extract_chinese_sentence(input_file_path, output_file_path):
    # Compile the regular expression pattern to match Chinese sentences
    regex_pattern = r"\s[A-Za-z']+\b[\s\S]*?[\u4e00-\u9fff]+\s*。"

    # Open the input file and read its contents line by line
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        file_lines = input_file.readlines()

    # Open the output file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # Loop over each line in the input file
        for line in file_lines:
            # Find all matches of the pattern in the current line
            matches = re.findall(regex_pattern, line)

            # Write the matched sentences to the output file
            for match in matches:
                output_file.write(match + '\n')

    # Return the number of matched sentences
    return len(matches)


input_file_path = 'paiwan_stripped.txt'
output_file_path = 'paiwan_stripped2.txt'

matched_sentence_count = extract_chinese_sentence(input_file_path, output_file_path)


