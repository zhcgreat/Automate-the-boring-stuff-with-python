#! python3

import re
checkuppercase = re.compile(r'[A-Z]')
checklowercase = re.compile(r'[a-z]')
checkdigit = re.compile(r'\d')
checklens = re.compile(r'.{8,}')
elif checklens.search(pwd) == None:
print ('Your password should be at least eight characters long.')
else:
print ('Your password is strong.')
def strongpwdcheck(pwd):
    if checkuppercase.search(pwd) == None:
        print ('Your password should contain upper case.')
    elif checklowercase.search(pwd) == None:
        print ('Your password should contain lower case.')
    elif checklens.search(pwd) == None:
        print ('Your password should be at least eight characters long.')
    else:
        print ('Your password is strong.')
