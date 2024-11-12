#Program 5(b)

print("Pyramid Printing")
rows=int(input("Enter number of Rows:"))
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
print("\n")
print("Inverted Pyramid Printing")
rows=int(input("Enter number of Rows:"))
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
print("\n")

Output :-

Pyramid Printing
Enter number of Rows:5
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 


Inverted Pyramid Printing
Enter number of Rows:5
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
        
#Program 5(c)
        
print("Program for Repeat a and b")
a=5
b=10
count=0
while count <a and count <b:
    print(f"count:{count},a:{a},b:{b}")
    count+=1
    
Output :-

Program for Repeat a and b
count:0,a:5,b:10
count:1,a:5,b:10
count:2,a:5,b:10
count:3,a:5,b:10
count:4,a:5,b:10
