#coding=utf-8
#! python3
# madlibs.py - Change specific word into another word.
import re
origintxt = 'origion.txt'
newtxt = 'new.txt'
place=re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
with open(origintxt, 'r') as o:
    contents=o.read()
    needreplace= place.findall(contents)
    if needreplace == []:
        print ("Can't find somewhere need to replace")
    else:
        for i in range(len(needreplace)):
            rp = input('Enter a %s' %(needreplace[i].lower()))
            contents=contents.replace(needreplace[i], rp, 1)
    print (contents)
    with open(newtxt, 'w') as n:
        n.write(contents)
