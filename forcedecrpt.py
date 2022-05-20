#! python
# forcedecrpt.py - Decrypt the PDF by trying every possible English word.

import PyPDF2

def forceDecrypt(password):
    pdfReader = PyPDF2.PdfFileReader(open('forcedecrypt.pdf', 'rb'))
    num = pdfReader.decrypt(password)
    return num


with open ('dictionary.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        num = forceDecrypt(line.upper())
        if num == 0:
            num = forceDecrypt(line.lower())
            if num == 0:
            print ('decrypting...')  #傻傻的等实在太无聊了，输出点东西感觉会好一点
            else:
                print ('The password is '+line.lower())
                break
        else:
            print ('The password is '+line.upper())
            break
