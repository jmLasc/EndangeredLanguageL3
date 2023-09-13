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




##def read_pdf_text(filename):
##    # Open the PDF file in read-binary mode
##    with open(filename, 'rb') as f:
##        # Create a PDF reader object
##        pdf_reader = PyPDF2.PdfFileReader(f) 
##        
##        # Loop through all pages in the PDF
####        for page_num in range(pdf_reader.getNumPages()):
##        for page_num in range(10): 
##            # Get the text of the page
##            page = pdf_reader.getPage(page_num)
##            page_text = page.extractText()
##            
##            # Split the page text into lines
##            lines = page_text.splitlines()
##            
##            # Remove lines containing the ★ character using the remove_star() function
##            filtered_lines = remove_star(lines)
##
##            # Remove numbered lines using the remove_numbered_lines() function
##            filtered_lines = remove_number(filtered_lines)
##
###this is repeated because there  are 1.1. and 2.2. -->by repeating it can get rid of the second repeated number 
##            filtered_lines = remove_number(filtered_lines)
##            
##            filtered_lines = remove_number_2(filtered_lines)
##            
##            # Remove lines containing a Chinese character followed by a period using the remove_chinese_dot() function
##            filtered_lines = remove_chinese_definition(filtered_lines)
##
##            # Remove Chinese characters followed by a space, an English period, and any number of whitespace characters using the remove_chinese_definition_space() function
##            filtered_lines = remove_chinese_definition_space(filtered_lines)
##
##            # Print the remaining lines
##            for line in filtered_lines:
##                if not re.search(r'(\bhttps://e-dictionary.ilrdf.org.tw\b)|([\u4e00-\u9fff]*阿美語[\u4e00-\u9fff]*)', line):
##                    print(line)
##
### Call the function with the input filename
##read_pdf_text('amis.pdf')

def read_pdf_text(filename):
    # Open the PDF file in read-binary mode
    with open(filename, 'rb') as f:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(f) 

        # Get the text of the 10th page
        page = pdf_reader.getPage(9) # Page numbering starts from 0, so page 10 is index 9
        page_text = page.extractText()

        # Split the page text into lines
        lines = page_text.splitlines()

        # Remove lines containing the ★ character using the remove_star() function
        filtered_lines = remove_star(lines)
        print(filtered_lines)
        print("")

##        # Remove numbered lines using the remove_numbered_lines() function
##        filtered_lines = remove_number(filtered_lines)
##        print(filtered_lines)
##        print("")
##
##        # Remove numbered lines again to handle cases like 1.1. or 2.2.
##        filtered_lines = remove_number(filtered_lines)
##        print(filtered_lines)
##        print("")
##
##        # Remove lines starting with a number and a period using the remove_number_2() function
##        filtered_lines = remove_number_2(filtered_lines)
##        print(filtered_lines)
##        print("")
##
##        # Remove lines containing a Chinese character followed by a period using the remove_chinese_definition() function
##        filtered_lines = remove_chinese_definition(filtered_lines)
##        print(filtered_lines)
##        print("")
##
##        # Remove Chinese characters followed by a space, an English period, and any number of whitespace characters using the remove_chinese_definition_space() function
##        filtered_lines = remove_chinese_definition_space(filtered_lines)
##        print(filtered_lines)
##        print("")
        
        # Print the remaining lines
        for line in filtered_lines:
            if not re.search(r'(\bhttps://e-dictionary.ilrdf.org.tw\b)|([\u4e00-\u9fff]*阿美語[\u4e00-\u9fff]*)', line):
                print(line)

# Call the function with the input filename
read_pdf_text('amis.pdf')
