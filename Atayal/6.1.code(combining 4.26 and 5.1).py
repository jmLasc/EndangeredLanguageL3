import PyPDF2
import re

def remove_star(lines):
    def filter_function(line):
        return "★" not in line and not re.search(r'(\bhttps://e-dictionary.ilrdf.org.tw\b)|([\u4e00-\u9fff]*泰雅語[\u4e00-\u9fff]*)', line)
    filtered_lines = filter(filter_function, lines)
    return list(filtered_lines)

def remove_number(lines): 
    pattern = "\d."
    filtered_lines = [re.sub(pattern, '', line) for line in lines]
    return filtered_lines

def remove_whitespace(lines):
    #pattern = "^\s *?\s"
    #pattern = "^\s+|\s$'"
    pattern = "^\s+|\s$"
    filtered_lines = [re.sub(pattern, '', line) for line in lines]
    return filtered_lines

#def take_chiense (lines):
#    for character in lines: 
#       if  
#        while  



def read_pdf_text(filename, stripped_output_file):
    with open(filename, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)

        with open(stripped_output_file, 'w', encoding='utf-8') as stripped_output: 
            for page_num in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page_num)
                page_text = page.extractText()

                lines = page_text.splitlines()

                stripped_lines = remove_star(lines)
                stripped_lines = remove_number(stripped_lines)
                stripped_lines = remove_whitespace(stripped_lines)
                for line in stripped_lines:
                    stripped_output.write(line + '\n')

#def read_pdf_text(filename, stripped_output_file):
    with open(filename, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)

        with open(stripped_output_file, 'w', encoding='utf-8') as stripped_output:
            if pdf_reader.getNumPages() > 0:  # Check if the PDF has at least one page
                page = pdf_reader.getPage(0)  # Get the first page
                page_text = page.extractText()

                lines = page_text.splitlines()
                stripped_lines = remove_star(lines)
                stripped_lines = remove_number(stripped_lines)
                stripped_lines = remove_whitespace(stripped_lines)

                for line in stripped_lines:
                    stripped_output.write(line + '\n')

read_pdf_text('atayal.pdf', 'atayal_stripped6.1.txt')


