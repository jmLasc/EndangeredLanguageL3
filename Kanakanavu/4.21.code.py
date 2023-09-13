import PyPDF2
import re

def remove_star(lines):
    # Define a function that filters out lines containing the ★ character
    def filter_function(line):
        return "★" not in line
    
    # Filter out lines containing the ★ character using the filter() function
    filtered_lines = filter(filter_function, lines)
    
    # Return the filtered lines
    return list(filtered_lines)

def remove_number(lines):
    # Define a regular expression pattern to match lines starting with a number and a period
    pattern = r'^(\s*)\d+\.(\s*\d+\.)*\s*'

    # Remove the pattern from lines using the re.sub() function
    filtered_lines = [re.sub(pattern, '', line) for line in lines]

    # Return the filtered lines
    return filtered_lines

#when I do this I have 2. left so this is meant to get rid of the 2. --> for some reason it is not working 

def remove_number_2(lines):
    # Define a regular expression pattern to match lines starting with a number and a period
    pattern = r'^\d+\.\s*'

    # Remove the pattern from lines using the re.sub() function
    filtered_lines = [re.sub(pattern, '', line) for line in lines]

    # Return the filtered lines
    return filtered_lines


def remove_chinese_definition(lines):
    # Define a regular expression pattern to match Chinese characters followed by an English period
    pattern = r'[\u4e00-\u9fff]+\.\s*'

    # Remove the pattern from lines using the re.sub() function
    filtered_lines = [re.sub(pattern, '', line) for line in lines]

    # Return the filtered lines
    return filtered_lines

def remove_chinese_definition_space(lines):
    # Define a regular expression pattern to match Chinese characters followed by one or more non-period characters, any number of spaces, a period, and any number of whitespace characters
    pattern = r'[\u4e00-\u9fff]+[^.\n]*\s*\.\s*'

    # Remove the pattern from lines using the re.sub() function
    filtered_lines = [re.sub(pattern, '', line) for line in lines]

    # Return the filtered lines
    return filtered_lines



def read_pdf_text(filename, output_file):
    # Open the PDF file in read-binary mode
    with open(filename, 'rb') as f:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(f) 
        
        # Create a new text file in write mode
        with open(output_file, 'w', encoding='utf-8') as output:
            # Loop through all pages in the PDF
##            for page_num in range(pdf_reader.getNumPages()):
            for page_num in range(456): 
                # Get the text of the page
                page = pdf_reader.getPage(page_num)
                page_text = page.extractText()
                
                # https://e-dictionary.ilrdf.org.tw Page 575 of 781Split the page text into lines
                lines = page_text.splitlines()
                
                # Remove lines containing the ★ character using the remove_star() function
                filtered_lines = remove_star(lines)

                # Remove numbered lines using the remove_numbered_lines() function
                filtered_lines = remove_number(filtered_lines)

                #this is repeated because there  are 1.1. and 2.2. -->by repeating it can get rid of the second repeated number 
                filtered_lines = remove_number(filtered_lines)

                filtered_lines = remove_number_2(filtered_lines)

                # Remove lines containing a Chinese character followed by a period using the remove_chinese_dot() function
                filtered_lines = remove_chinese_definition(filtered_lines)

                # Remove Chinese characters followed by a space, an English period, and any number of whitespace characters using the remove_chinese_definition_space() function
                filtered_lines = remove_chinese_definition_space(filtered_lines)

                # Write the remaining lines to the output file
                for line in filtered_lines:
                    if not re.search(r'(https://e-dictionary.ilrdf.org.tw\b)|([\u4e00-\u9fff]*卡那卡那富語[\u4e00-\u9fff]*)', line):
                        output.write(line + '\n')


# Call the function with the input filename
read_pdf_text('kanakanavu.pdf', 'kanakanavu_filtered.txt')

