__author__ = 'Tejal'

import os
import re

inputdir = 'C:\\Users\\Tejal\\Documents\\NACC\\UDS2Migration\\output1\\csv'

for subdir, dirs, files in os.walk(inputdir):
    for file in files:
        fname = inputdir+"\\"+file

        lines = []

        f = open(fname,"r")
        while True:
            # print("line")
            line = f.readline()
            if not line:
                break
            else:
                line = re.sub('\.0,', ',', line)
                line = re.sub('\.0\\n', '\\n', line)
                # line = re.sub('"\."', '', line) #when you want field to be blank instead of 0
                line = re.sub('"\."', '0', line)
                # print(line)
                lines.append(line)
        f.close()

        f = open(fname,"w")
        for line in lines:
            print(line)
            f.write(line)
        f.close()