import PyPDF2
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

def read_pdf_text(filename, stripped_output_file, end_chars):
    with open(filename, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)

        with open(stripped_output_file, 'w', encoding='utf-8') as stripped_output: 
            for page_num in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page_num)
                page_text = page.extractText()

                lines = page_text.splitlines()

                for line in lines:
                    result = copy_substring(line, end_chars)
                    if result is not None:
                        stripped_output.write(result + '\n')

end_chars = ["。", "？", "！"]  # Specify the list of end characters

read_pdf_text('atayal.pdf', 'atayal_stripped6.2.txt', end_chars)
