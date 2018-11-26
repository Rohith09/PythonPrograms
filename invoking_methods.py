class A:
    def car(self):
        print("Prints a car!")

    def bike(self):
        self.car()
        print("Prints a bike")


A().bike()