# Class definition for a Room Object

class Room:

    # Constuctor
    def __init__(self, room_number, price_per_hour):
        self.room_number     =  room_number
        self.price_per_hour  =  price_per_hour
        self.song_list       =  []
        self.current_guests  =  []
        self.room_max        =  2

    # Methods.

    def add_song(self, new_song):
        """ Method that adds a new song to the rooms song list. """ 
        self.song_list.append(new_song)

    def get_song_list_len(self):
        """ Mehtod that returns the current length of the somg list. """
        return len(self.song_list)

    def add_guest(self, new_guest):
        """ Method that adds a guest to the room. """ 
        self.current_guests.append(new_guest)

    def get_current_guest_list_len(self):
        """ Method that returns how many people are curently in a room. """
        return len(self.current_guests)

    def check_if_room_full(self):
        """ Method that checks if the room is at max capacity. """ 
        if self.get_current_guest_list_len() >= self.room_max:
            return True 
        else: 
            return False 

    def guest_check_in(self, guest):
        """ Method that utalises helper methods to check a customer into a room/pay"""
        if self.check_if_room_full() == False:
            if guest.can_pay_bill(self) == True:
                guest.pay_bill(self.price_per_hour)
                self.add_guest(guest)
            else:
                
                return "You require more funds." 
        else:
            return "I'm sorry, this room is currently full, please try another."

 
    
