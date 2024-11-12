from tabulate import tabulate
import xlrd
import os
stu_list='salary.xls'
book=xlrd.open_workbook(stu_list)
sh=book.sheet_by_index(0)
r=sh.nrows
c=sh.ncols
da=[]
for i in range(r):
    d=[]
    for j in range(c):
        if j==0 or j==1 or j==3 or j==8:
            d.append(sh.cell(i,j).value)
    da.append(d)
print(tabulate(da,headers="firstrow",tablefmt="grid"))
    
Output :-

+------------+----------+----------+----------+
| emp_Name   |   Emp_id |   Emp_Bp |   Netpay |
+============+==========+==========+==========+
| Sathish    |     2050 |    30000 |  54375   |
+------------+----------+----------+----------+
| Sharan     |     2051 |    31000 |  56187.5 |
+------------+----------+----------+----------+
| Sharmila   |     2052 |    35000 |  63437.5 |
+------------+----------+----------+----------+
| Sherin     |     2053 |    30100 |  54556.2 |
+------------+----------+----------+----------+
