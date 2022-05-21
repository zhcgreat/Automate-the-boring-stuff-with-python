#! python
# coding =utf-8
# removeCsvHeader.py - Removes the header from all CSV files in the current working directory

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files.
    print ('Removing header from ' + csvFilename + '...')
    # Reader CSV file in (skipping first row).
    csvRows = []
    with open(csvFilename) as c:
        reader = csv.reader(c)
        for row in reader:
            if reader.line_num == 1:
                continue    # skip first row
            csvRows.append(row)
            # Write out the CSV file.
            with open(os.path.join('headerRemoved', csvFilename), 'w', newline='') as newcsv:
                csvWriter = csv.writer(newcsv)
                for row in csvRows:
                    csvWriter.writerow(row)
