# Class definition for a guest object.

class Guest:

    def __init__(self, name, age, wallet):
        self.name   =  name 
        self.age    =  age 
        self.wallet =  wallet

    def pay_bill(self, amount):
        self.wallet -= amount