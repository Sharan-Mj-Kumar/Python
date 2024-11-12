class shapes:
    def define(self):
        print("Program to find Area of Rectangle,Square,Triangle...")
class rectangle(shapes):
    def area(self):
    	length=int(input("Enter Length of a Rectangle:"))
    	width=int(input("Enter Width of a Rectangle:"))
        print("Area of Rectangle:",length*width)
class square(shapes):
    def area(self):
    	side=int(input("Enter Side of a Square:"))
        print("Area of Square",side*side)
class triangle(shapes):
    def area(self):
    	base=int(input("Enter Base of a Triangle:"))
    	height=int(input("Enter Height of a Triangle:"))
        print("Area of Triangle:",0.5*base*height)
r=rectangle()
s=square()
t=triangle()
r.define()
r.area()
s.area()
t.area()

Output :-

Program to find Area of Rectangle,Square,Triangle...
Enter Length of a Rectangle:5
Enter Width of a Rectangle:5
Area of Rectangle: 25
Enter Side of a Square:4
Area of Square 16
Enter Base of a Triangle:4
Enter Height of a Triangle:6
Area of Triangle: 12.0
