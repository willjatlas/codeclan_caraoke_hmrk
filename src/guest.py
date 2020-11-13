# Class definition for a guest object.

class Guest:

    # Constructor.
    def __init__(self, name, age, wallet):
        self.name   =  name 
        self.age    =  age 
        self.wallet =  wallet

    # Methods.

    def can_pay_bill(self, room):
        """ Checks if a customer has the funds to pay for the room. """ 
        if self.wallet >= room.price_per_hour:
            return True 
        else: 
            return False

    def pay_bill(self, amount):
        """ Method that allows the customer to pay thier bill. """ 
        self.wallet -= amount
