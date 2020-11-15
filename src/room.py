# Class definition for a Room Object

class Room:

    # Constuctor
    def __init__(self, room_number, price_per_hour):
        self.room_number     =  room_number
        self.price_per_hour  =  price_per_hour
        self.song_list       =  []
        self.current_guests  =  []
        self.room_max        =  2
        self.till            =  0 

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

    def add_room_payment(self):
        """ Method that increases the till by the room price per hour """
        self.till += self.price_per_hour

    def get_songs_by_title(self, title):
        """ Method that returns a list of song objects when given a title """
        output = []
        for song in self.song_list:
            if song.title == title:
                output.append(song)
        if len(output) == 0:
            return "Sorry, we do not have that song"
        else:
            return output
        
    def get_songs_by_artist(self, artist):
        """ Method that returns a list of songs by a given artist. """
        output = [] 
        for song in self.song_list:
            if song.artist == artist:
                output.append(song)
        if len(output) == 0:
            return "Sorry, we don't have anything by that artist"
        else: 
            return output

    def guest_check_in(self, guest):
        """ Method that utalises helper methods to check a customer into a room/pay"""
        if self.check_if_room_full() == False:
            if guest.can_pay_bill(self) == True:
                guest.pay_bill(self.price_per_hour)
                self.add_room_payment()
                self.add_guest(guest)
            else: 
                return "You require more funds." 
        else:
            return "I'm sorry, this room is currently full, please try another."

 
    
