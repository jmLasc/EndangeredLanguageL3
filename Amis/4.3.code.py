import PyPDF2
import re

def read_pdf_text(filename):
    # Open the PDF file in read-binary mode
    with open(filename, 'rb') as f:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(f) 
        
        # Loop through all pages in the PDF
##        for page_num in range(pdf_reader.getNumPages()):
        for page_num in range(3): 
            # Get the text of the page
            page = pdf_reader.getPage(page_num)
            page_text = page.extractText()
            
            # Split the page text into lines
            lines = page_text.splitlines()

            # Create an empty list to accumulate the lines that don't contain the repeated parts
            filtered_lines = []
            
            # Loop through each line and remove lines that contain the specific repeated part or the Chinese character
            for line in lines:
                if not re.search(r'(\bhttps://e-dictionary.ilrdf.org.tw\b)|([\u4e00-\u9fff]*阿美語[\u4e00-\u9fff]*)', line):
                    # If the line doesn't contain the specific repeated parts, add it to the filtered lines
                    filtered_lines.append(line)
            
            # Join the filtered lines into a single string and return it
            filtered_text = '\n'.join(filtered_lines)
            
        return filtered_text


def remove_chinese_definition(text):
    # Create a regular expression pattern to match the desired pattern
    pattern = r'\d+\.[\u4e00-\u9fff]+\.'

    # Use the sub() function to replace all matches of the pattern with an empty string
    result = re.sub(pattern, '', text)

    print(result)



text= read_pdf_text('amis.pdf')
remove_chinese_definition(text) 
