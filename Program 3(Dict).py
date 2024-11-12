n=int(input('Enter Number of Students:'))
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
dic={}
c=0
for i in stumark:
    ave=sum(i)/len(i)
    dic[stuname[c]]=ave
    c+=1
sortdic=sorted(dic.items(), key=lambda x:x[1],reverse=True)
print('\t\tTop 3 Ranked Students:\n')
for i in range(len(sortdic)):
    name,mark=sortdic[i]
    print(i+1,name,"\t:",mark)
    if i+1==3:
        break
        
Output :-

Enter Number of Students:4
Enter Student name: Sharan
Enter the Subject mark(for 100): 60
Enter the Subject mark(for 100): 65
Enter the Subject mark(for 100): 70
Enter the Subject mark(for 100): 75
Enter the Subject mark(for 100): 80
Enter Student name: Kumar 
Enter the Subject mark(for 100): 65
Enter the Subject mark(for 100): 70
Enter the Subject mark(for 100): 75
Enter the Subject mark(for 100): 80
Enter the Subject mark(for 100): 85
Enter Student name: Sathish
Enter the Subject mark(for 100): 60
Enter the Subject mark(for 100): 70
Enter the Subject mark(for 100): 65
Enter the Subject mark(for 100): 75
Enter the Subject mark(for 100): 80
Enter Student name: Simion
Enter the Subject mark(for 100): 70
Enter the Subject mark(for 100): 75
Enter the Subject mark(for 100): 80
Enter the Subject mark(for 100): 85
Enter the Subject mark(for 100): 90

         Top 3 Ranked Students:

	1 Simion 	: 80.0
	2 Kumar  	: 75.0
	3 Sharan 	: 70.0
