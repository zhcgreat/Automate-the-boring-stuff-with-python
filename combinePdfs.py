#! python
# combinePdfs.py - Combines all the PDFs in the current working directory into a single PDF.

import os, PyPDF2

# Get all the PDF filenames.
pdffiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdffiles.append(filename)
pdffiles.sort(key=str.lower)
pdfWrite = PyPDF2.PdfFileWriter()
# Loop through all the PDF files.
for pdffile in pdffiles:
    pdfObj = open(pdffile, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfObj)
    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWrite.addPage(pageObj)

# Save the resulting PDF to a file.
pdfOutput = open('allminutes.pdf', 'wb')
pdfWrite.write(pdfOutput)
pdfOutput.close()
