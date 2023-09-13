import string

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
            end_index = i  
            substring = line[start_index:end_index + 1]  
            return substring
        i += 1  
    return None  

def read_text_file(filename, stripped_output_file, end_chars):
    with open(filename, 'r', encoding='utf-8') as text_file:
        with open(stripped_output_file, 'w', encoding='utf-8') as stripped_output: 
            for line in text_file:
                result = copy_substring(line, end_chars)
                if result is not None:
                    stripped_output.write(result + '\n')

end_chars = ["。", "？", "！"]  # Specify the list of end characters

read_text_file('atayal_stripped6.9.txt', 'atayal_stripped6.9.(2.0).txt', end_chars)
