#! python
# excel_csv.py - Convert excel file to csv file.

import csv, openpyxl, os

os.makedirs('csv', exist_ok=True)
for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object.
    if not excelFile.endswith('.xlsx'):
        continue
    print ('Converting ' + excelFile +'...')
    wb = openpyxl.load_workbook(excelFile)
    for sheetName in wb.sheetnames:
        # Loop through every sheet in the workbook.
        sheet = wb[sheetName]
        filename = excelFile[:-5]+'_'+sheetName+'.csv'
        # Create the CSV filename from the Excel filename and sheet title.
        with open(os.path.join('csv', filename), 'w', newline='') as c:
            csvWriter = csv.writer(c)
            # Loop through every row in the sheet.
            for rowNum in range(1, sheet.max_row + 1):
                rowData = [] # append each cell to this list
                # Loop through each cell in the row.
                for colNum in range(1, sheet.max_column + 1):
                    # Append each cell's data to rowData.
                    rowData.append(sheet.cell(rowNum,colNum).value)
                # Write the rowData list to the CSV file.
                csvWriter.writerow(rowData)
