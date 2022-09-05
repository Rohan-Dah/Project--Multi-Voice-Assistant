class BA:
    def _init_(self):
        self.cn=""
        self.ca=""
        self.an=0
        self.cb=0
        
    def creatacc(self,CN,CA,AN,CB):
        self.cn=CN
        self.ca=CA
        self.an=AN
        self.cb=CB
        
    def chbl(self):
        print("customer name=",self.cn)
        print("customer address=",self.ca)
        print("customer account no=",self.an)
        print("customer bank balance=",self.cb)
        
    def upbl(self):
        print("customer updated balance is",self.cb)
        
class BT(BA):
    def _init_(self):
        BA._init_(self)
        
    def withdraw(self,v):
        self.cb=self.cb-v
        
    def diposit(self,v):
        self.cb=self.cb+v
        
obj=BT()
choise=0

while(choise!=5):
    choise=int(input("enter your choise: 1=create account  2=check balance  3=deposit  4=withdraw  5=exit  "))

    if(choise==1):
        CN=input("enter the name=")
        CA=input("enetr the address=")
        AN=int(input("enter the account number="))
        CB=int(input("enter the initial balance="))
        obj.creatacc(CN,CA,AN,CB)
        
    if(choise==2):
        obj.chbl()
        
    if(choise==3):
        v=int(input('enter the ammount to be deposite='))
        obj.diposit(v)
        obj.upbl()
        
    if(choise==4):
        v=int(input('enter the ammount to be withdraw='))
        obj.withdraw(v)
        obj.upbl()