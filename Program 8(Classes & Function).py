class xyz_bank:
    def __init__(self,balance):
        self.customer_name=input("Enter Name:")
        self.acc_no=input("Enter Account Number:")
        self.acc_type=input("Enter acount Type(senior-citizen/minor/general):")
        self.balance=balance
    def choice(self):
        self.choice=input("Enter Choice credit or debit or check-balance:")
        if self.choice == "credit" or "Credit" or "CREDIT":
            amount=int(input("Enter Credit amount:"))
            if amount>0:
                self.balance += amount
                print("Money Credited-Available Balance:",self.balance)
            else:
                print("Invalid amount")
        elif self.choice == "debit" or "Debit" or "DEBIT":
            amount=int(input("Enter Debit amount:"))
            if amount >0 and amount <= (self.balance-100):
                self.balance-=amount
                print("Money is Debited-Available Balance:",self.balance)
            else:
                print("Insufficient Balance")
        elif self.choice == "check-balance" or "balance":
            print("Available Balance :",self.balance)
        else:
            print("Invalid Choice")
    def open_term_deposit(self):
        if self.acc_type == "senior-citizen" or "Senior-Citizen" or "SENIOR-CITIZEN" or "senior" or "Senior" or "SENIOR":
            intrest = 0.12
        else:
            intrest = 0.10
            principle=200
            year=5
            si = principle*year*intrest
            total_amount=principle+si
            print("Open term Deposit amount:",total_amount)
    def display(self):
        print("\nCustomer name:",self.customer_name,"\nAccount number:",self.acc_no,"\nAccount Type:",self.acc_type)
c1=xyz_bank(1000)
c1.choice()
c1.open_term_deposit()
c1.display()

Output :-

Enter Name:Sharan
Enter Account Number:498598770
Enter acount Type(senior-citizen/minor/general):minor
Enter Choice credit or debit or check-balance:credit
Enter Credit amount:500
Money Credited-Available Balance: 1500

Customer name: Sharan 
Account number: 498598770 
Account Type: minor
