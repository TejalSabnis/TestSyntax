__author__ = 'Tejal'

import xlrd
import csv
import os
import win32com.client as win32

rootdir = 'C:\\Users\\Tejal\\Documents\\NACC\\UDS2Migration\\input'

outputdir = 'C:\\Users\\Tejal\\Documents\\NACC\\UDS2Migration\\output1'

f = open(outputdir+'\\script\\'+"script.txt","w")
f2 = open(outputdir+'\\script\\'+"drop_table_script.txt","w")

scriptString = "mysqlimport --local --delete --fields-terminated-by=, --lines-terminated-by='\\n' --fields-optionally-enclosed-by='\"' --ignore-lines=1 -p -u root uds_test "

for subdir, dirs, files in os.walk(rootdir):
    for file in files:

        fname = rootdir+"\\"+file
        excel = win32.gencache.EnsureDispatch('Excel.Application')
        wb = excel.Workbooks.Open(fname)

        wb.SaveAs(fname+"x", FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
        wb.Close()                               #FileFormat = 56 is for .xls extension
        excel.Application.Quit()

        filename_without_ext = file.split(".")
        wb = xlrd.open_workbook(rootdir+"\\"+filename_without_ext[0]+".xlsx")
        sh = wb.sheet_by_index(0)
        # print(sh.cell(1,1).value)
        your_csv_file = open(outputdir+'\\csv\\'+sh.cell(1,1).value.lower()+'_uds_v2.csv', 'wb')
        wr = csv.writer(your_csv_file, quoting=csv.QUOTE_NONNUMERIC)

        for rownum in xrange(sh.nrows):
            print(sh.row_values(rownum))
            wr.writerow(sh.row_values(rownum))

        your_csv_file.close()

        f.write(scriptString+sh.cell(1,1).value.lower()+'_uds_v2.csv'+'\n\n')
        f2.write("DROP TABLE IF EXISTS '"+sh.cell(1,1).value.lower()+"_uds_v2';\n")