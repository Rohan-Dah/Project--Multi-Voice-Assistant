'''import pyttsx3
friend = pyttsx3.init()
friend.say("Greetings Mr. Rohan. How May i help you")
friend.runAndWait()'''

class BankAccount:
    def _init_(self):
        self.AccNo=0
        self.CusName=""
        self.CusAdd=""
        self.Balance=0
        
    def CreateAccount(self,AN,CN,CA,Bal):
        self.AccNo=AN
        self.CusName=CN
        self.CusAdd=CA
        self.Balance=Bal
    
    def CheckBalance(self):
        print("Customer Account No. : ",self.AccNo)
        print("Customer Name : ",self.CusName)
        print("Customer Address : ",self.CusAdd)
        print("Customer Account Balance : ",self.Balance)
        
    def UpdatedBalance(self):
        print("Updated Bank Balance : ",self.Balance)
        
class BankTransaction(BankAccount):
    def _init_(self):
        BankAccount._init_(self)
        
    def Withdraw(self,value):
        self.Balance = self.Balance - value
        
    def Deposit(self,value):
        self.Balance = self.Balance + value
        
obj = BankTransaction()
choice=0
while(choice!=5):
    print("\n 1. Create Account \n 2. Check Account Balance \n 3. Withdraw \n 4. Deposit \n 5. Exit")
    choice=int(input("Enter Your Choice : "))
    if (choice==1):
        AccNo=int(input("Enter the Account No. : "))
        CusName=input("Enter the Customer Name : ")
        CusAdd=input("Enter Customer Address : ")
        intbalance=int(input("Enter the Initial Balance : "))
        obj.CreateAccount(AccNo,CusName,CusAdd,intbalance)
        
    elif(choice==2):
        obj.CheckBalance()
        
    elif(choice==3):
        value=int(input("Enter the amount to withdraw : "))
        obj.Withdraw(value)
        obj.UpdatedBalance()
        
    elif(choice==4):
        value=int(input("Enter the amount to deposit : "))
        obj.Deposit(value)
        obj.UpdatedBalance()