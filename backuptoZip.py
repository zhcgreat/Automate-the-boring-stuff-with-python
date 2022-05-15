#! python3
# backuptoZip.py - Copies an entire folder and its contents into a Zip file whose filename increments.

import zipfile, os

def backuptoZip(folder):
    # Backup the entire contents of 'folder' into a Zip file.
    folder = os.path.abspath(folder) #make sure folder is absolute.
    # Figure out the filename this code should base on.
    # What files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder)+'_' + str(number)+".zip"
        if not os.path.exists(zipFilename):
            break
        number = number + 1
    #Creat the Zip file.
    print ('Creating %s...' %(zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Wlaking the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print ('Adding files in %s...' % (foldername))
        # Add the current folder to the zip file.
        backupZip.write(foldername)
        # Add all the files in this folder to the zip file.
        for filename in filenames:
            newBase=os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't backup the zip files.
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print ('Done')

backuptoZip('D:\\py\\automate')
