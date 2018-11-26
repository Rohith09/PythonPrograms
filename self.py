class Mobile:
    def __init__(self, price, brand):
        print("Id of self in constructor", id(self))
        self.price = price
        self.brand = brand


mob1 = Mobile(1000, "Apple")
print("Id of mob1 in driver code", id(mob1))
mob1.design = "Circular"
print("Design of the Mobile is"+mob1.design)
mob2 = Mobile(1000, "Apple")
print("Id of mob2 in driver code", id(mob2))
