n=input('Enter the Numbers: ')
c=n.split()
char=list(set(c))
result=[]
for i in char:
    cou=0
    li=[]
    li.append(i)
    for j in c:
        if i==j:
            cou+=1
    li.append(cou)
    result.append(li)
result.sort(key=lambda x:x[1],reverse=True)
print(result)
print('Result in list:',result)
print("Highest Occerence of digit is: ",result[0]," in ",result[0][1],"times")
print("Least Occerence of digit is: ",result[len(result)-1]," in ",result[len(result)-1][1],"time")

Output :-

Enter List Of Numbers: 2 3 4 5 3 4 2 6 7 6 5 4 3

[['4', 3], ['3', 3], ['5', 2], ['6', 2], ['2', 2], ['7', 1]]

Result in list: [['4', 3], ['3', 3], ['5', 2], ['6', 2], ['2', 2], ['7', 1]]

Highest Occerence of digit is:  ['4', 3]  in  3 times

Least Occerence of digit is:  ['7', 1]  in  1 time
