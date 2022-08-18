from pdf2docx import Converter

# PDF file to convert
pdf_file = './samples/sample.pdf'

# Output file name - should be an empty .docx
docx_file = './samples/sample.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()