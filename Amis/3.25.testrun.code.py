import PyPDF2
import re
import docx


def remove_chinese(text):
    # Remove any Chinese characters from the text
    return re.sub(r'[\u4e00-\u9fff。，、` ？-]+|[0-9]+', '', text)

def read_pdf_text(filename):
    # Open the PDF file in read-binary mode
    with open(filename, 'rb') as f:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(f) 
        
        # Loop through all pages in the PDF
        for page_num in range(pdf_reader.getNumPages()):
            # Get the text of the page
            page = pdf_reader.getPage(page_num)
            page_text = page.extractText()

##            #strip away the indents and white spaces
            page_text = re.sub(r'\n\s*\n', '\n', page_text)
            page_text = re.sub(r'\n+', '\n', page_text)
            page_text = str(page_text.strip())           
            
            # Remove any Chinese characters from the text
            page_text = remove_chinese(page_text)
            
            # Print the text
            print(page_text)

def strip_chinese_from_pdf(filename):
    # Open the PDF file in read-binary mode
    with open(filename, 'rb') as f:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(f)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfFileWriter()

        # Loop through all pages in the PDF
        for page_num in range(pdf_reader.numPages):
            # Get the text of the page
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()

            # Remove any Chinese characters from the text
            page_text = remove_chinese(page_text)

            # Add the updated page to the PDF writer
            pdf_writer.addPage(page)

        # Save the updated PDF to a new file
        with open('stripped_' + filename, 'wb') as output_file:
            pdf_writer.write(output_file)

    # Open the stripped PDF file in read-binary mode
    with open('stripped_' + filename, 'rb') as f:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfFileReader(f)

        # Loop through all pages in the PDF
        for page_num in range(pdf_reader.numPages):
            # Get the text of the page
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()

            # Remove any Chinese characters from the text
            page_text = remove_chinese(page_text)

            # Return the updated text of the page
            return page_text


from docx import Document
def create_word_doc(filename, text):
    # Create a new Word document
    doc = Document()

    # Add the stripped text to the document
    doc.add_paragraph(text)

    # Save the document
    doc.save(filename)

#top level code
read_pdf_text('amis1.pdf')
strip_chinese_from_pdf('amis1.pdf')

stripped_text = strip_chinese_from_pdf('amis1.pdf')
create_word_doc('amis1.docx', stripped_text)




