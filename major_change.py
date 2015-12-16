from collections import Counter

import openpyxl
from openpyxl.cell import column_index_from_string


read_file = 'Major-School-College-Change-8.xlsx'
write_file = 'table.txt'

wb = openpyxl.load_workbook(read_file)
sheet = wb.worksheets[0]
row_count = sheet.get_highest_row() - 1
all_codes = {}

# 2 semester major sequence code: BQ, 69

#set up dictionary
for row_num in range(1, row_count):
   code = sheet.cell(row=row_num, column=64).value
   all_codes[code] = all_codes.get(code, 0) + 1
   
num_elems = len(all_codes)

# convert to google charts format
with open(write_file, 'wb') as wf:

   for key in all_codes:
      if len(key) > 1:
         elem = key[1]
      else:
         elem = '-'
         
      wf.writelines(['[\'' + key[0] + '\', \'' + elem + '\', ' + str(all_codes[key]) + '],\n'])