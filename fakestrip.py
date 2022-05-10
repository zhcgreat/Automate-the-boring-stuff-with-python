#coding=utf-8
import re
def stripRegex():
    str1 = input('Please put in your text')
    del1 = input('what do you want to delete?')
    if del1 == '':
        deleteBlank = re.compile(r'\S')
        mo = deleteBlank.findall(str1)
        print(''.join(mo))
    else:
        a = '^'+del1
        b = del1 + '$'
        changestr1 = re.compile(a)
        mo = changestr1.sub('', str1)
        changestr2 = re.compile(b)
        mo = changestr2.sub('', mo)
        print (mo)
