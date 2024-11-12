n=int(input('Enter the Number of Series:'))
a=-1
b=1
c=0
i=0
if n==0:
    print('Fibonacci series is 0')
elif n<0:
    print('Enter valid Number')
else:
    while i<n:
        c=a+b
        print(c)
        a=b
        b=c
        i+=1

Output :-

Enter the Number of Series:5
0
1
1
2
3
