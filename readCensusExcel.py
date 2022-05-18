#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for each county.

import openpyxl, pprint
print ('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countryData = {}

# Fill in countyData with each county's population and tracts
print ('Reading rows')
for row in range(2, sheet.max_row+1):
    # Each row in the spreadsheet has data for one census tract
    state = sheet['B' + str(row)].value
    country = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure the key for this state exists.
    countryData.setdefault(state, {})
    # Make sure the key for this country in this state exists.
    countryData[state].setdefault(country, {'tracts':0, 'pop':0})
    # Each row represents one census tract. so increment by one.
    countryData[state][country]['tracts'] += 1
    # Increase the country pop by the pop in this census tract.
    countryData[state][country]['pop'] += int(pop)

# Open a new text file and write the contents of countryData to it.
print ('Writing results...')
with open('census2010.py', 'w') as resultFile:
    resultFile.write('allData = ' + pprint.pformat(countryData))
print ('Done')
