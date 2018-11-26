class Mobile:
    def __init__(mob1):
        print("Inside the Mobile constructor")
        mob1.brand = None
        brand = "Apple"
        #This is a local variable.
        #Variables without self are local and they dont
        #affect the attributes.
        print("The brand is "+brand)

        #Local varaibles cannot be accessed outside the init
        #Using self creates attributes which are
        #accessible in other methods as well

    def cycle(self):
        print("The brand of the cycle is"+self.brand)


mob1 = Mobile()
print(mob1.brand)

#This does not print Apple
#This prints None because brand=Apple creates
#a local variable and it does not affect the attribute