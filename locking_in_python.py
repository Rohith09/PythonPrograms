class Customer:
    def __init__(self,name,age,balance):
        self.name=name
        self.age=age
        self.__balance=balance

    def show_balance(self):
        print("The balance amount in the account is " + str(self.__balance))


c = Customer("Rohith", 21, 325435654523332465789)
c._Customer__balance = 1234567890
c.show_balance()
