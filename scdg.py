#! python3
# coding=utf-8
# scdg.py - Choose specific file to copy or delete files and close or insert gap(s)
# python scdg.py copy                    - Copy specific files to another folder.
# python scdg.py delete                  - Delete filenames that is bigger than 100M
# python scdg.py closegaps               - close all gaps.
# python scdg.py insertgap               - insert a gap.

import os, send2trash, shutil, re, sys
def selectiveCopy(folder, item):
    folder = os.path.abspath(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        print ('Searching %s...' %(foldername))
        for filename in filenames:
            if filename.endswith(item):
                absWorkingDir = os.path.abspath(foldername)
                filename = os.path.join(absWorkingDir, filename)
                print ('\tCopying ' + filename + '...')
                shutil.copy(filename, 'Copied')
    print ('Done')

def selectiveDelete(folder):
    folder = os.path.abspath(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        print ('Searching %s ...' %(foldername))
        for filename in filenames:
            absWorkingDir = os.path.abspath(foldername)
            filename = os.path.join(absWorkingDir, filename)
            if os.path.getsize(filename) > 100*1024*1024: #os.path.getsize返回的是字节，需换算
                #send2trash.send2trash('filename')
                print ('\tdeleting %s...' %(filename))
    print ('Done')

def reName(folder,oldername, newname):
    absWorkingDir = os.path.abspath(folder)
    oldername= os.path.join(absWorkingDir, oldername)
    newname = os.path.join(absWorkingDir, newname)
    shutil.move(oldername,newname)


def closeGaps(folder, beforePart):
    number = []
    ma = '^' + beforePart + "(\d+)(.*?)$"
    numRegex = re.compile(ma)
    for filename in os.listdir(folder):
        mo = numRegex.search(filename)
        if mo == None:
            continue
        number.append(int(mo.group(1)))
        afterpart=mo.group(2)


    for i in range(sorted(number)[-1]):
        if i+1 not in number:
            missing = beforePart+str(i+1).rjust(3,'0')+afterpart
            oldername = beforePart+str(i+2).rjust(3,'0')+afterpart
            newname = missing
            if i+2 in number:  #如果下下个数字的文件也不存在就不处理，靠while True回头再处理
                reName(folder,oldername, newname)
    return number

def insertGap(folder, gap, beforePart):
    number = []
    ma = '^' + beforePart + "(\d+)(.*?)$"
    numRegex = re.compile(ma)
    for filename in os.listdir(folder):
        mo = numRegex.search(filename)
        if mo == None:
            continue
        number.append(int(mo.group(1)))
        afterpart=mo.group(2)
    number.sort(reverse=True)
    a = number.index(gap)
    for i in range(a+1):
        oldername = beforePart+str(number[i]).rjust(3,'0')+afterpart
        number[i] = number[i]+1
        newname = beforePart+str(number[i]).rjust(3,'0')+afterpart
        reName(folder,oldername, newname)

if sys.argv[1].lower() == 'copy':
    item = input ('please entern the extension')
    selectiveCopy('.', item)

elif sys.argv[1].lower() == 'delete':
    selectiveDelete('.')

elif sys.argv[1].lower() == 'closegaps':
    prefix = input('Please enter the prefix')
    while True:
        number = closeGaps('.', prefix)
        if len(number) == sorted(number)[-1]:
            break

elif sys.argv[1].lower() == 'insertgap':
    gap = int(input('Please enter the gap'))
    beforePart = input('Please ent the prefix')
    insertGap('.', gap, beforePart)
