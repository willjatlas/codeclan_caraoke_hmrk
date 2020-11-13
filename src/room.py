# Class definition for a Room Object

class Room:

    # Constuctor
    def __init__(self):
        self.song_list       = []
        self.current_guests  = []

    # Methods.

    def add_song(self, new_song):
        """ Method that adds a new song to the rooms song list. """ 
        self.song_list.append(new_song)

    def get_song_list_len(self):
        """ Mehtod that returns the current length of the somg list. """
        return len(self.song_list)

    def add_guest(self, new_guest):
        self.current_guests.append(new_guest)