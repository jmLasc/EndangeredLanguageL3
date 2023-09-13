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
            
            # Loop through each line and remove lines that contain the specific repeated part
            for line in lines:
                 if not re.search(r'(\bhttps://e-dictionary.ilrdf.org.tw\b)|([\u4e00-\u9fff]*阿美語[\u4e00-\u9fff]*)', line):
                    # If the line doesn't contain the specific repeated parts, print the line
                    print(line)




text= read_pdf_text('amis.pdf')
remove_pattern_chinese(text)
