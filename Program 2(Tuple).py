n=int(input('Enter Number of Student:'))
name=()
int_m=()
sem=()
assign=()
mark=()
total=0
for i in range(n):
    li=[]
    na=input('Enter the name:')
    name=(*name,na)#unpacking
    for j in range(3):
        li.append(int(input('Enter mark:')))
    li=sorted(li,reverse=True)
    int_m=(*int_m,li)
    sem=(*sem,(int(input('Enter seminar mark:'))))
    assign=(*assign,(int(input('Enter Assignment mark:'))))
for k in range(n):
    intmark=sum(int_m[k][0:2])/2
    total=intmark+sem[i]+assign[i]
    print("Total Percentage :",total)
    mark=(*mark,total)
    
print("Name\tIntnl mark(best two)\tSeminar mark\tAssignmk Mark\t Total")
for i in range(n):
    print(name[i],"\t",int_m[i][0:2],"\t\t",sem[i],"\t\t",assign[i],"\t\t",mark[i])
print(int_m)
print(name)
print(sem)
print(assign)
print(mark)

Output :-

Enter Number of Student:2
Enter the name:Sharan
Enter Internal mark(25):20
Enter Internal mark(25):22
Enter Internal mark(25):21
Enter seminar mark:5
Enter Assignment mark:5
Enter the name:Kumar
Enter Internal mark(25):19
Enter Internal mark(25):22
Enter Internal mark(25):21
Enter seminar mark:5
Enter Assignment mark:5
Total Percentage : 31.5
Total Percentage : 31.5
Name	Intnl mark(best two)	Seminar mark	Assignmk Mark	 Total
Sharan 	 [22, 21] 		 5 		 5 		 31.5
Kumar 	 [22, 21] 		 5 		 5 		 31.5
([22, 21, 20], [22, 21, 19])
('Sharan', 'Kumar')
(5, 5)
(5, 5)
(31.5, 31.5)
