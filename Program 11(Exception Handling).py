#ZeroDivision Error
try:
    num1=int(input("Enter the Numerator:"))
    num2=int(input("Enter the Denaminator:"))
    div=num1/num2
    print("Division of Two Numbers:",div)
except ZeroDivisionError:
    print("!!...Zero Division is Not Possible")
except:
    print("!!...Same error has Occured")

#File-access-error

try:
    fname=input("Enter the file Name:")
    f=open(fname,'r')
    print(f.read())
    print("File Occured")
except IOError:
    print("!!...File not found")
    
#list index Out-of-Range
try:
    li=[]
    n=int(input("Enter the Number of Element:"))
    for i in range(n):
        e=int(input("Enter the Elements:"))
        li.append(e)
    print(li)
    ch=int(input("Enter the index number You want view the Element:"))
    print("Index no:{}:{}".format(ch,li[ch]))
except IndexError:
    print("Oops...!!! List index Out of Range")
except:
    print("!...Some error has Occured")
    
Output:-

Enter the Numerator:4
Enter the Denaminator:2
Division of Two Numbers: 2.0

Enter the file Name:notfound
!!...File not found

Enter the Number of Element:4
Enter the Elements:1
Enter the Elements:2
Enter the Elements:3
Enter the Elements:4

[1, 2, 3, 4]

Enter the index number You want view the Element:2
Index no:2:3
