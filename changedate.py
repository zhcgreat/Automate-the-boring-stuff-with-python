#! python3
# renameDates.py - Rename filenames with American MM-DD-YYYY date format to YYYY-MM-DD.

import shutil, os, re

# Creat a regex that matches files with the American date format.
datePattern = re.compile(r'''
    ^(.*?)                                    # all text before the date.
    ((0|1)?\d)-                               # one or two digitals for the month
    ((0|1|2|3)?\d)-                           # one or two digitals for the day
    ((19|20)\d\d)                             # four digits for the year
    (.*?)$                                    # all text after the date
    ''', re.VERBOSE)

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Skip files without date.
    if mo == None:
        continue
    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthpart = mo.group(2)
    daypart = mo.group(4)
    yearpart = mo.group(6)
    afterpart = mo.group(8)

    # Form the YYYY-MM-DD style filename.
    yyyymmdd = beforePart+yearpart+'-'+monthpart+'-'+daypart+afterpart
    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    yyyymmdd = os.path.join(absWorkingDir, yyyymmdd)

    # Rename the files.
    print ('Renaming "%s" to "%s" ...'% (amerFilename, yyyymmdd))
    #shutle.move(amerFile, yyyymmdd)                                # uncomment after testing.
