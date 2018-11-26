class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def purchase(self):
        print("Hello There")
        print(self.brand)
        print(self.price)


mob = Mobile("Apple",2142314)
mob.purchase()
print(mob.price)
print(mob.brand)

