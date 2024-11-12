from tabulate import tabulate
import csv
def units(s,e):
    unit=int(e)-int(s)
    if unit<=50:
        cost=unit*30
    elif unit<=100:
        cost=(50*30)+(unit-50)*35
    elif unit<=150:
        cost=(50*30)+(50*35)+(unit-100)*40
    else:
        cost=(50*30)+(50*35)+(50*40)+(unit-150)*50
    return cost
with open('eb-bill.csv','r') as f:
    csvfile=csv.reader(f)
    head=['customer-Id','Customer-name','Total-Cost']
    da=[]
    next(csvfile)
    for li in csvfile:
        tu=units(li[2],li[3])
        da.append([li[0],li[1],tu])
    print(tabulate(da,headers=head,tablefmt='grid'))


Output :-
 
+---------------+-----------------+--------------+
|   customer-Id | Customer-name   |   Total-Cost |
+===============+=================+==============+
|             1 | Sharan          |         3250 |
+---------------+-----------------+--------------+
|             2 | Sathish         |         3250 |
+---------------+-----------------+--------------+
|             3 | Simion          |        -3000 |
+---------------+-----------------+--------------+
|             4 | Velmurugan      |        12750 |
+---------------+-----------------+--------------+
|             5 | Viswa           |        -6000 |
+---------------+-----------------+--------------+
