import PyPDF2

# First open the PDF file
with open('example.pdf', 'rb') as file:
    # Now create a PDF reader object
    reader = PyPDF2.PdfReader(file)
    
    # Next open a new text file to write the plain text
    with open('example.txt', 'w') as text_file:
        # Iterate over all the pages in the PDF
        for page_number in range(len(reader.pages)):
            # Get the current page
            pdf_page = reader.pages[page_number]
            # Extract the plain text from the page
            text = pdf_page.extract_text()
            # Write the text to the text file
            text_file.write(text)
