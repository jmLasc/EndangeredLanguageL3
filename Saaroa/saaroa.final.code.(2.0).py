import PyPDF2
import re
import string

# Updated 4.26 code
def remove_star(lines):
    return [line for line in lines if "★" not in line and not re.search(r'(\bhttps://e-dictionary.ilrdf.org.tw\b)|([\u4e00-\u9fff]*拉阿魯哇語[\u4e00-\u9fff]*)', line)]

def remove_number(lines):
    pattern = r'^(\s*)\d+\.(\s*\d+\.)*\s*'
    return [re.sub(pattern, '', line) for line in lines]

def remove_chinese_definition(lines):
    pattern = r'[\u4e00-\u9fff]+\.\s*'
    return [re.sub(pattern, '', line) for line in lines]

def remove_chinese_definition_space(lines):
    pattern = r'[\u4e00-\u9fff]+[^.\n]*\s*\.\s*'
    return [re.sub(pattern, '', line) for line in lines]

def remove_american_periods_after_chinese_punctuations(lines):
    # Regular expression to remove American periods following Chinese punctuations
    pattern = r'([。！？])\s*\.\s*'
    return [re.sub(pattern, r'\1', line) for line in lines]


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


# Updated 6.9 code
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
                        current_line = remove_american_periods_after_chinese_punctuations([current_line])[0]  # Remove American period after Chinese punctuation
                        stripped_output.write(current_line + '\n')
                    current_line = line
                elif should_log:
                    if line:
                        current_line += ' ' + line
                    else:
                        current_line = remove_american_periods_after_chinese_punctuations([current_line])[0]  # Remove American period after Chinese punctuation
                        stripped_output.write(current_line + '\n')
                        current_line = ''
            if current_line:
                current_line = remove_american_periods_after_chinese_punctuations([current_line])[0]  # Remove American period after Chinese punctuation
                stripped_output.write(current_line + '\n')

# Updated 6.12 code
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

# Updated 6.13.(2.0) code
def transcribe_lines(input_file, output_file):
    with open(input_file, "r") as input_file:
        lines = input_file.readlines()

    output_lines = []
    current_line = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        if line.startswith(("'", '"')) or line[0].isalpha():
            current_line += line + " "
        else:
            # Add this line to remove American periods after Chinese punctuations
            line = remove_american_periods_after_chinese_punctuations([line])[0]

        if current_line and (not line or line[0].isdigit()):
            current_line = remove_american_periods_after_chinese_punctuations([current_line])[0]  # Add this line to remove American periods
            output_lines.append(current_line.strip())
            current_line = ""

    if current_line:
        current_line = remove_american_periods_after_chinese_punctuations([current_line])[0]  # Add this line to remove American periods
        output_lines.append(current_line.strip())

    with open(output_file, "w") as output_file:
        for line in output_lines:
            output_file.write(line + "\n")

# 4.26 code
read_pdf_text('saaroa.pdf', 'saaroa_stripped_1.txt')

# 6.9 code
read_text_file('saaroa_stripped_1.txt', 'saaroa_stripped(1.1).txt')

# 6.12 & 6.13 code
input_file = "saaroa_stripped(1.1).txt"
output_file_1 = "saaroa_stripped(2.1).txt"
output_file_2 = "saaroa_stripped(3.1).txt"
regex_pattern_1 = r"([\u4e00-\u9fff]+\. )|([\u4e00-\u9fff]+ \.)|([\u4e00-\u9fff]+\S\.)|[\u4e00-\u9fff]+\S \.|[\u4e00-\u9fff]+\S \. |[\u4e00-\u9fff]+\S\. |(\u2026\u2026\.)|(\s\)\.\s)|(\s\）\.\s)|(\.\)\.)"
regex_pattern_2 = r' [2-9]'
add_newlines(input_file, output_file_1, regex_pattern_1)
add_return_bar_before_regex(regex_pattern_2, output_file_1, output_file_2)

# 6.13.(2.0) code
transcribe_lines(output_file_2, "saaroa_stripped_final_1.txt")
