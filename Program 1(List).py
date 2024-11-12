n=int(input('Enter number of Students:'))
stuname=[]
stumark=[]
for i in range(n):
    name=input('Enter Student name: ')
    stuname.append(name)
    t=[]
    for j in range(5):
        marks=int(input('Enter the Subject mark(for 100): '))
        t.append(marks)
    stumark.append(t)
per=[]
print(stuname)
print(stumark)
for i in stumark:
    ave=sum(i)/len(i)
    per.append(ave)
c=0
print('\n')
print(per)
print('\nName \t Percentage \t Performance\n')
for i in per:
    if i>=90 and i<=100:
        print(stuname[c],'\t\t',per[c],'\t Excellent Performance ')
    elif i<=89 and i>=70:
        print(stuname[c],'\t\t',per[c],'\t Very Good Performance')
    elif i<=69 and i>=50:
        print(stuname[c],'\t\t',per[c],'\t Good Performance ')
    elif i<=49:
        print(stuname[c],'\t\t',per[c],'\t need improvment ')
    c+=1
    
Output :-
 
Enter number of Students:2
Enter Student name: Sharan
Enter the Subject mark(for 100): 60
Enter the Subject mark(for 100): 70
Enter the Subject mark(for 100): 75
Enter the Subject mark(for 100): 85
Enter the Subject mark(for 100): 90
Enter Student name: Kumar
Enter the Subject mark(for 100): 60
Enter the Subject mark(for 100): 65
Enter the Subject mark(for 100): 70
Enter the Subject mark(for 100): 75
Enter the Subject mark(for 100): 80
    
['Sharan', 'Kumar']

[[60, 70, 75, 85, 90], [60, 65, 70, 75, 80]]


[76.0, 70.0]

Name 	 Percentage 	 	Performance

Sharan 		 76.0 	 Very Good Performance
Kumar 		 70.0 	 Very Good Performance
