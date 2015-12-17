import time
from collections import OrderedDict

import pandas as pd

start_time = time.time()

read_file = '../Major-School-College-Change 8.csv'
write_file = 'sankey_py.html'

code_col_name = 'sch_seq_6'
gender_col_name = 'sex'
mcode_col_contents = []
fcode_col_contents = []

num_letters = 6

df = pd.read_csv(read_file)

#get gender, code

for row in df.itertuples():
   if row[4] == 'M':
      mcode_col_contents.append([row[64], len(row[64])])
   else:
      fcode_col_contents.append([row[64], len(row[64])])

#define html tags
body = """<html>
   <body>
      <script type="text/javascript"
      src="https://www.google.com/jsapi?autoload={'modules':[{'name':'visualization','version':'1.1','packages':['sankey']}]}">
      </script>
      <h1>Male</h1>
      <div id="sankey_1" style="width: 900px; height: 300px;"></div>
      <br>
      <br>
      <h1>Female</h1>
      <div id="sankey_2" style="width: 900px; height: 300px;"></div>
      
"""  
script_begin = """<script type="text/javascript">
      google.setOnLoadCallback(drawChart);
      function drawChart() {
          var data1 = new google.visualization.DataTable();
          data1.addColumn('string', 'From');
          data1.addColumn('string', 'To');
          data1.addColumn('number', 'Weight');
          data1.addRows([
"""

script_middle = """
       var data2 = new google.visualization.DataTable();
       data2.addColumn('string', 'From');
       data2.addColumn('string', 'To');
       data2.addColumn('number', 'Weight');
       data2.addRows([
"""  

    
 
script_end2 = """

   var options = {
      width: 600,
   };
   
   var chart1 = new google.visualization.Sankey(document.getElementById('sankey_1'))
   var chart2 = new google.visualization.Sankey(document.getElementById('sankey_2'))
   chart1.draw(data1, options);
   chart2.draw(data2, options);
  
   }
   </script>
   </body>
   </html>
"""



#convert to google charts format
def write_chart(gender, contents):
   for idx in range(num_letters): 
      codes = OrderedDict()
      for curr_cell in contents:
         full_code = curr_cell[0]
         full_code_len = curr_cell[1]
         if full_code_len > idx + 1:
            code = str(full_code[idx]) + str(full_code[idx+1])
            codes[code] = codes.get(code, 0) + 1
         else:
            contents.remove(curr_cell)
      for key in codes:
         str_to_write = '\t\t\t\t\t[\'' + key[0] + str(idx+1) + '\', \'' + key[1] + str(idx+2)+ '\', ' + str(codes[key]) + ']'
         if idx + 1 == num_letters - 1 and codes.keys().index(key) == len(codes) - 1:
               pass
         else:
            str_to_write += ','
         str_to_write += '\n'
         wf.write(str_to_write)

   wf.write(']);')
               
with open(write_file, 'wb') as wf:
   initial_html = body + script_begin
   wf.write(initial_html)
   write_chart('F', fcode_col_contents)
   wf.write(script_middle)
   write_chart('M', mcode_col_contents)
   wf.write(script_end2)
   

  

print "Time to complete:" + str(time.time() - start_time)
