class ATMCard:
    def __init__(self, card_number,name, pin, balance):
        self.card_number = card_number
        self.name =name
        self.pin = pin
        self.balance = balance
        self.attempts = 0

    def swipe_card(self, entered_pin, amount):
        if self.attempts >= 3:
            self.calling_police()
            return "Account is locked due to too many wrong PIN attempts. Police have been notified."
       
        if entered_pin == self.pin:
            if amount > self.balance:
                return "Insufficient balance."
            self.balance -= amount
            return 'Withdrew',amount,'from your account. Available balance:',self.balance
        else:
            self.attempts += 1
            return "Wrong PIN!!!. Attempts remaining: ",3 - self.attempts

    def check_balance(self, entered_pin):
        if entered_pin == self.pin:
            return "Your account balance is ",self.balance
        else:
            return "Wrong PIN. Please enter the correct PIN to check your balance."

    def calling_police(self):
        print("!!!..Calling the police to report... a potential ATM card theft or misuse!!!.")
       
try:
    print('Enter your details..')
    no=input('Enter your account NO: ')
    name=input('Enter your name: ')
    pin=int(input('Set a pin number(4digit): '))
    balance=int(input('Enter the balance amount: '))
    atm_card = ATMCard(no,name,pin,balance)# Create an ATM card instance
       
    while True:
        ch=int(input('\nEnter your choice: \n1.Swipe card \n2.check balance \n3.Exit'))
        if ch==1:
            apin=int(input('Enter your pin no: '))
            abalance=int(input('Enter amount you want to withdraw: '))
            print(atm_card.swipe_card(apin,abalance))
        elif ch==2:
            apin=int(input('Enter your pin no: '))
            print(atm_card.check_balance(apin))
        elif ch==3:
            break
        else:
            print('Entet valid choice...')
except IOError:
    print('Somethink wents to wrong..')
    
Output :-
    
    Enter Your Details :-
Enter Your Account NO: 498598334
Enter Your name: Sharan Kumar
Set a PIN Number(4digit): 4455

1.Swipe card 
2.check balance 
3.Exit 
Enter your choice: 1
Enter Your PIN no: 4455
Enter Withdraw amount: 100
('Withdraw', 100, 'from your account. Available balance:', 900)

1.Swipe card 
2.check balance 
3.Exit 
Enter your choice: 1
Enter Your PIN no: 4334
Enter Withdraw amount: 100
('Wrong PIN Number. Attempts remaining: ', 2)

1.Swipe card 
2.check balance 
3.Exit 
Enter your choice: 2
Enter your PIN no: 4455
('Your account balance is ', 900)

1.Swipe card 
2.check balance 
3.Exit 
Enter your choice: 2
Enter your PIN no: 4334
Wrong PIN. Please enter the correct PIN to check your balance.

1.Swipe card 
2.check balance 
3.Exit 
Enter your choice: 3
Exited
