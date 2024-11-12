from abc import ABC, abstractmethod
# Abstract Shop class
class Shop(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show_menu(self):
        pass
       
    @abstractmethod
    def make_bill(self, order,qnty):
        pass

# Derived class Mobile_Shop
class Mobile_Shop(Shop):
    def __init__(self, name):
        super().__init__(name)

    def show_menu(self):
        mess= "\n Mobiles, Accessories and Gadgets Menu \n 1. Oneplus 7 - Rs. 30,000 \n 2. Realme 8 Pro - 18,000"
        print(mess)

    def make_bill(self, order,qnty):
        if order == 1:
        	mess=f"Customer name: {self.name} \n Product name : Oneplus 7 \n Price : Rs. {30000 * qnty}"
        	print(mess)
        elif order == 2:
        	mess=f"Customer name: {self.name} \n Product name : Realme 8 Pro \n Price : Rs. {18000 * qnty}"
        	print(mess)

# Derived class Coffee_Shop
class Coffee_Shop(Shop):
    def __init__(self, name):
        super().__init__(name)

    def show_menu(self):
        mess= "\n Coffee and Beverages Menu \n 1. Badam Milk - Rs. 50 \n 2. Chocolate Coffee - Rs. 100"
        print(mess)
    def make_bill(self, order,qnty):
        if order == 1:
        	mess= f"Customer name: {self.name} \n Product name : Badam Milk \n Price : Rs. {50 * qnty}"
        	print(mess)
        elif order == 2:
        	mess= f"Customer name: {self.name} \n Product name : Chocolate Coffee \n Price : Rs. {100 * qnty}"
        	print(mess)

# Derived class Cake_Shop
class Cake_Shop(Shop):
    def __init__(self, name):
        super().__init__(name)

    def show_menu(self):
        mess = "\n Cakes and Pastries Menu \n 1. Black-Current(1 KG) - Rs. 350 \n 2. Black Forest(1 KG) - Rs. 700"
        print(mess)
    def make_bill(self, order,qnty):
        if order == 1:
        	mess= f"Customer name: {self.name} \n Product name : Black-Current(1 KG)\n Price : Rs.{350 * qnty}"
        	print(mess)
        elif order == 2:
        	mess= f"Customer name: {self.name} \n Product name : Black Forest(1 KG) \n Price : Rs. {700 * qnty}"
        	print(mess)

# Polymorphic function to display menu and make a bill
def visit_shop(Shop):
    Shop.show_menu()
    #print("\n Enter the Corresponding number for make Payment:")
    order = int(input("\n Enter Your Choice: "))
    qnty= int(input("\n Enter Number of Quantity: "))
    if order == 1 or order == 2:
    	print("\n          ... Your Bill ...")
    	print("------------------------------------------")
    	Shop.make_bill(order,qnty)
    	print("------------------------------------------")
    else:
    	print("None")
print("Welcome to A to Z Super Market")
cname= input("Enter Your name: ")

# Create instances of different shop types
mobile_shop = Mobile_Shop(cname)
coffee_shop = Coffee_Shop(cname)
cake_shop = Cake_Shop(cname)

# Visit and interact with each shop
visit_shop(mobile_shop)
visit_shop(coffee_shop)
visit_shop(cake_shop)

Output :-

Welcome to A to Z Super Market
Enter Your name: Sharan Kumar

 Mobiles, Accessories and Gadgets Menu 
 1. Oneplus 7 - Rs. 30,000 
 2. Realme 8 Pro - 18,000

 Enter Your Choice: 1

 Enter Number of Quantity: 2

          ... Your Bill ...
------------------------------------------
Customer name: Sharan Kumar 
 Product name : Oneplus 7 
 Price : Rs. 60000
------------------------------------------

 Coffee and Beverages Menu 
 1. Badam Milk - Rs. 50 
 2. Chocolate Coffee - Rs. 100

 Enter Your Choice: 2

 Enter Number of Quantity: 4

          ... Your Bill ...
------------------------------------------
Customer name: Sharan Kumar 
 Product name : Chocolate Coffee 
 Price : Rs. 400
------------------------------------------

 Cakes and Pastries Menu 
 1. Black-Current(1 KG) - Rs. 350 
 2. Black Forest(1 KG) - Rs. 700

 Enter Your Choice: 1

 Enter Number of Quantity: 1

          ... Your Bill ...
------------------------------------------
Customer name: Sharan Kumar 
 Product name : Black-Current(1 KG)
 Price : Rs.350
------------------------------------------
