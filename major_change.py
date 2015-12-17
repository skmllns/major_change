import time
from collections import OrderedDict

import pandas as pd

read_file = 'Major-School-College-Change 8.csv'
write_file = 'sankey.html'
col_name = 'sch_seq_6'
col_contents = []
num_letters = 6

start_time = time.time()

df = pd.read_csv(read_file)
for cell in df[col_name]:
   col_contents.append([cell, len(cell)])

#convert to google charts format
with open(write_file, 'wb') as wf:
   body = """<html>
   <body>
      <script type="text/javascript"
      src="https://www.google.com/jsapi?autoload={'modules':[{'name':'visualization','version':'1.1','packages':['sankey']}]}">
      </script>

      <div id="sankey_multiple" style="width: 900px; height: 300px;"></div>

      <script type="text/javascript">
      google.setOnLoadCallback(drawChart);
      function drawChart() {
          var data = new google.visualization.DataTable();
          data.addColumn('string', 'From');
          data.addColumn('string', 'To');
          data.addColumn('number', 'Weight');
          data.addRows(['
   """
   wf.write(body)
   for idx in range(num_letters): 
      codes = OrderedDict()
      for curr_cell in col_contents:
         full_code = curr_cell[0]
         full_code_len = curr_cell[1]
         if full_code_len > idx + 1:
            code = str(full_code[idx]) + str(full_code[idx+1])
            codes[code] = codes.get(code, 0) + 1
         else:
            col_contents.remove(curr_cell)
      for key in codes:
         str_to_write = '\t\t\t\t\t[\'' + key[0] + str(idx+1) + '\', \'' + key[1] + str(idx+2)+ '\', ' + str(codes[key]) + ']'
         if idx + 1 == num_letters - 1 and codes.keys().index(key) == len(codes) - 1:
               pass
         else:
            str_to_write += ','
         str_to_write += '\n'
         wf.write(str_to_write)
   footer = """      ]);

    // Set chart options
    var options = {
      width: 600,
    };

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.visualization.Sankey(document.getElementById('sankey_multiple'));
    chart.draw(data, options);
   }
   </script>
   </body>
   </html>
   """
   wf.write(footer)
       
print "Time to complete:" + str(time.time() - start_time)
