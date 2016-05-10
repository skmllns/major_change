########################################################################################
## 12/2015 - SKM
##
## HTML: https://developers.google.com/chart/interactive/docs/gallery/sankey
##
## Creates Sankey diagram based on sequence codes
## Currently looking at school change sequence codes of length=6, separated by gender
##
#########################################################################################

import pandas as pd

#i/o
read_file = '../Major-School-College-Change 8.csv'
write_file = 'sankey_py.html'

#choose appropriate column names
code_col_name = 'sch_seq_6'
gender_col_name = 'sex'

#create lists to separate m/f
mcode_col_contents = []
fcode_col_contents = []

#max_length of sequence code
num_letters = 6

#read the file into a pandas dataframe, for efficiency
df = pd.read_csv(read_file)

#get gender, code
#itertuples iterates over the rows as tuples
#create a list of lists of sequence codes and their length
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

#input: gender, sequence codes with that gender code
#output: writes individual node-weight groups to a file
def write_chart(gender, contents):

   #look at each pair of letters, up to the maximum code length
   for idx in range(num_letters): 
      #create a dictionary for nodes and weights
      codes = {}  

      #this list will be useful if the order of nodes could be somehow set 
      sorted_codes = []                              
      
      #look at each code/length pairing
      for curr_cell in contents:                   
         full_code = curr_cell[0]
         full_code_len = curr_cell[1]
         
         #test if there are enough letters in this idx position to make a pair
         if full_code_len >= idx + 1:
            if full_code_len > idx + 1:
               code = str(full_code[idx]) + str(full_code[idx+1])
            #if there's only one letter in the pair:
            #if the student finished all semesters:
            elif full_code_len == num_letters: 
               contents.remove(curr_cell)
            #else, add a blank to indicate the student didn't return the next semester,
            #and remove it 
            else:
               code = str(full_code[idx]) + '-'
               contents.remove(curr_cell)
            
            #make a dictionary of nodes and weights
         codes[code] = codes.get(code, 0) + 1
        
      #for future implementation (refer to above). how the heck do you sort dicts with lambda?
      for elem in sorted(codes):                  
         sorted_codes.append([elem, codes[elem]])
         
      #convert to google charts format: [node-start, node-finish, weight],
      for pos in sorted_codes:
			str_to_write = '\t\t\t\t\t[\'' + pos[0][0] + str(idx+1) + '\', \'' + pos[0][1] + str(idx+2) + '\', ' + str(pos[1]) + ']' 
         #check if this is the very very last element in the entire list of sequence codes
         #if so, don't add a comma separator
			#print idx

			if idx == num_letters - 1 and sorted_codes.index(pos) == len(sorted_codes) - 1:
				print "last idx"
				pass
			else:
				str_to_write += ','
			str_to_write += '\n'
			wf.write(str_to_write)

   wf.write(']);')

#concatenate html with sankey diagram information   
with open(write_file, 'wb') as wf:
   initial_html = body + script_begin
   wf.write(initial_html)
   write_chart('F', fcode_col_contents)
   wf.write(script_middle)
   write_chart('M', mcode_col_contents)
   wf.write(script_end2)
