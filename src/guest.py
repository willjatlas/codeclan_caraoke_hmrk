# Class definition for a guest object.

class Guest:

    # Constructor.
    def __init__(self, name, age, wallet):
        self.name   =  name 
        self.age    =  age 
        self.wallet =  wallet

    # Methods.
    
    def pay_bill(self, amount):
        """ Method that allows the customer to pay thier bill. """ 
        self.wallet -= amount