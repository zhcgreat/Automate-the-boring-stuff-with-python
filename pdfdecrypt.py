#! python
# pdfdecrypt.py - Decrypt all the pdf files in the (sub)folder.

import PyPDF2, os

password = input("Enter Pdf's password")
    for foldername , subfolders, filenames in os.walk('.'):
        for filename in filenames:
            if filename.endswith('.pdf'):
            print ('Decrypting '+filename+' ...')
            absWorkingDir = os.path.abspath(foldername)
            filename = os.path.join(absWorkingDir, filename)
            pdfFile = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            try:
                pdfReader.decrypt(password)
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))
                resultPdf = open(filename[:-13]+'decrypted.pdf', 'wb')
                pdfWriter.write(resultPdf)
                resultPdf.close()
                pdfFile.close()
            except PyPDF2.errors.PdfReadError:
                print (filename+"'s password isn't right.")

print ('Done')
