from collections import Counter
import time

from openpyxl import load_workbook

read_file = 'Major-School-College-Change 8.xlsx'
write_file = 'table.txt'

start_time = time.time()
wb = load_workbook(filename=read_file, read_only=True)
sheet = wb[wb.get_sheet_names()[0]]

row_count = sheet.max_row

# 6 semester major sequence code: BJ, 62
num_letters = 6

# convert to google charts format
with open(write_file, 'wb') as wf:
   # for total # of pairs possible,
   for idx in range(num_letters): 
      codes = {}
      # get pair from a code
      #look at every row
      for row_num in range(2, row_count):
         # get current row's code
         curr_cell = sheet.cell(row=row_num, column=64)
         # check the code length
         code_len = len(curr_cell.value)
         # check if there's a letter in the idx position
         if code_len > (idx + 1):
            code = str(curr_cell.value[idx]) + str(curr_cell.value[idx+1])
            codes[code] = codes.get(code, 0) + 1
         else:
            pass
         print codes, idx
         # for key in codes:
            # str_to_write = '[\'' + key[0] + str(idx+1) + '\', \'' + key[1] + str(idx+2)+ '\', ' + str(codes[key]) + '],\n'
            # wf.write(str_to_write)
      