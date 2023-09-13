import PyPDF2
import re
import string

#4.26code
def remove_star(lines):
    return [line for line in lines if "★" not in line and not re.search(r'(\bhttps://e-dictionary.ilrdf.org.tw\b)|([\u4e00-\u9fff]*泰雅語[\u4e00-\u9fff]*)', line)]

def remove_number(lines):
    pattern = r'^(\s*)\d+\.(\s*\d+\.)*\s*'
    return [re.sub(pattern, '', line) for line in lines]

def remove_chinese_definition(lines):
    pattern = r'[\u4e00-\u9fff]+\.\s*'
    return [re.sub(pattern, '', line) for line in lines]

def remove_chinese_definition_space(lines):
    pattern = r'[\u4e00-\u9fff]+[^.\n]*\s*\.\s*'
    return [re.sub(pattern, '', line) for line in lines]

def read_pdf_text(filename, stripped_output_file):
    with open(filename, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f) 
        
        with open(stripped_output_file, 'w', encoding='utf-8') as stripped_output:
            for page_num in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page_num)
                page_text = page.extractText()
                
                lines = page_text.splitlines()
                
                stripped_lines = remove_star(lines)
                for line in stripped_lines:
                    stripped_output.write(line + '\n')

#6.9 code
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

#6.12 code & 6.13 code
def add_newlines(input_file, output_file, regex_pattern):
    with open(input_file, "r", encoding="utf-8") as file:
        data = file.read()

    # Detect and add new lines after the regular expression match
    new_data = re.sub(regex_pattern, r"\1\n", data)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(new_data)


def add_return_bar_before_regex(regex_pattern, input_file, output_file):
    # Read the content from the input file
    with open(input_file, 'r') as file:
        text = file.read()

    # Add the return bar before the occurrences of the regex pattern
    updated_text = re.sub(regex_pattern, r'\n\g<0>', text)

    # Write the updated text to the output file
    with open(output_file, 'w') as file:
        file.write(updated_text)

#6.13.(2.0) code 
def transcribe_lines():
    with open("atayal_stripped(3.0).txt", "r") as input_file:
        lines = input_file.readlines()

    output_lines = []
    current_line = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        if line.startswith(("'", '"')) or line[0].isalpha():
            current_line += line + " "
        elif current_line:
            output_lines.append(current_line.strip())
            current_line = ""

    if current_line:
        output_lines.append(current_line.strip())

    with open("atayal_stripped_final.txt", "w") as output_file:
        for line in output_lines:
            output_file.write(line + "\n")

#4.26 code
read_pdf_text('atayal.pdf', 'atayal_stripped.txt')

#6.9 code 
read_text_file('atayal_stripped.txt', 'atayal_stripped(1.0).txt')

#6.12 & 6.13 code 
input_file = "atayal_stripped(1.0).txt"
output_file_1 = "atayal_stripped(2.0).txt"
output_file_2 = "atayal_stripped(3.0).txt"
regex_pattern_1 = r"([\u4e00-\u9fff]+\. )|([\u4e00-\u9fff]+ \.)|([\u4e00-\u9fff]+\S\.)|[\u4e00-\u9fff]+\S \.|[\u4e00-\u9fff]+\S \. |[\u4e00-\u9fff]+\S\. "
regex_pattern_2 = r' [2-9]'
add_newlines(input_file, output_file_1, regex_pattern_1)
add_return_bar_before_regex(regex_pattern_2, output_file_1, output_file_2)

#6.13.(2.0) code
transcribe_lines()



