import re

def add_newlines(input_file, output_file, regex_pattern):
    with open(input_file, "r", encoding="utf-8") as file:
        data = file.read()

    # Detect and add new lines after the regular expression match
    new_data = re.sub(regex_pattern, r"\1\n", data)

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(new_data)

    print("New file created:", output_file)


# Usage example
input_file = "atayal_stripped6.9.txt"
output_file = "atayal_stripped6.12.lateruse.txt"
regex_pattern = r"([\u4e00-\u9fff]+\. )|([\u4e00-\u9fff]+ \.)|([\u4e00-\u9fff]+\S\.)|[\u4e00-\u9fff]+\S \.|[\u4e00-\u9fff]+\S \. |[\u4e00-\u9fff]+\S\. "

add_newlines(input_file, output_file, regex_pattern)

