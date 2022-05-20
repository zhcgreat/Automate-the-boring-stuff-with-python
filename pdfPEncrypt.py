#! python
# pdfPEncrypt.py - go through every PDF in a folder (and its subfolders) and encrypt the PDFs

import os, PyPDF2, sys

password = sys.argv[1]
for foldername , subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            print ('Encrypting'+filename+'...')
            absWorkingDir = os.path.abspath(foldername)
            filename = os.path.join(absWorkingDir, filename)
            pdfFile = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
            pdfWriter.encrypt(password)
            resultPdf = open(filename[:-4]+'_encrypted.pdf', 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()
            pdfFile.close()

print ('Done')
