class Store:
    discount=30

    def __init__(self,name,total_amount):
        self.name = name
        self.total_amount = total_amount


def calculate_bill_with_discount(self):
    print("The total billing amount is ", self.total_amount)
    self.bill = self.total_amount-(self.total_amount*(Store.discount)/100)
    print("The total bill after discount is ", self.bill)


def calculate_bill_without_discount(self):
    Store.discount=0
    self.bill_without_disc=self.total_amount-(self.total_amount*(Store.discount)/100)
    print("The total bill without discount is ", self.bill_without_disc)


peter = Store("Peter",1000)
calculate_bill_with_discount(peter)
calculate_bill_without_discount(peter)