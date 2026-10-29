class Bank:
    def __init__(self, balance):
        self.balance = balance
        # i can also add here extra eventhoug it is not in the parameter in init
        self.min_withdraw = 100
        self.max_withdraw = 100000


    def get_balance(self):
        return self.balance # i can access any attribute from any method. as we have accesed here balance attribute from this method
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print (f'You can not withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print (f'you can not withdraw more than that in single transation {self.max_withdraw}')
        else:
            self.balance -= amount
            print (f'here is your money {amount}')
            print (f'your balance after widthdraw: {self.get_balance()}')


dbbl = Bank(15000)
dbbl.withdraw(25)
dbbl.withdraw(10000000)
dbbl.withdraw(1200)


ibbl = Bank(20000)
ibbl.deposite(2000)
ibbl.deposite(2000)
print(dbbl.get_balance())