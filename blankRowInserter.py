#! python
# coding=utf-8
# blankRowInserter.py -Insert blank row(s).
import openpyxl
filename = input('Please enter the filename')
N = int(input('Row to start'))
M = int(input('How many rows do you want to insert?'))
wb = openpyxl.load_workbook(filename)
sheet=wb.active
sheet.insert_rows(N,M)
wb.save('New'+filename)
