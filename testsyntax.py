__author__ = 'Tejal'

import re
import csv
import os

inputdir = 'C:\\Users\\Tejal\\Documents\\NACC\\UDS2Migration\\output1\\csv'

f = open(inputdir+"\\A2_uds_v2.csv","r")
lines = []

while True:
    # print("line")
    line = f.readline()
    line = re.sub(',"\.', ',"0', line)
    if not line:
        break
    else:
        print(line)
        lines.append(line)
f.close()

f = open(inputdir+"\\A2_uds_v2.csv","w")
for line in lines:
    f.write(line);
f.close()

# for subdir, dirs, files in os.walk(inputdir):
#     for file in files:
#         fname = inputdir+"\\"+file
#
#         new_rows = [] # a holder for our modified rows when we make them
#         changes = {   # a dictionary of changes to make, find 'key' substitute with 'value'
#             '.' : '0', # I assume both 'key' and 'value' are strings
#             }
#
#         with open(fname, 'rb') as f:
#             reader = csv.reader(f) # pass the file to our csv reader
#             for row in reader:     # iterate over the rows in the file
#                 new_row = row      # at first, just copy the row
#                 for index, element in enumerate(new_row):
#                     if(element=="."):
#                         new_row[index] = 0
#                 # for key, value in changes.items(): # iterate over 'changes' dictionary
#                 #     new_row = [ x.replace(key, value) for x in new_row ] # make the substitutions
#                 # print(new_row)
#                 new_rows.append(new_row) # add the modified rows
#
#         with open(fname, 'wb') as f:
#             # Overwrite the old file with the modified rows
#             writer = csv.writer(f)
#             writer.writerows(new_rows)
#
#         f.close()