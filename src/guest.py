# Class definition for a guest object.

class Guest:

    # Constructor.
    def __init__(self, name, age, wallet, favourite_song):
        self.name           =  name 
        self.age            =  age 
        self.wallet         =  wallet
        self.favourite_song = favourite_song
        self.current_exp    = 0
        self.skill_level    = 0

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

    def look_for_fav_song(self, room):
        """ Method that lets the customer look for their favourite song in a room"""
        for song in room.song_list:
            if self.favourite_song == song.title:
                return "DIS MY JAM!"
    
    def level_up(self):
        """ Method to increase the guests skill level """ 
        self.skill_level += 1 

    def reset_current_exp(self):
        """ Method to adjust current exp after level up """ 
        self.current_exp = 0

    def increase_exp(self, amount):
        """ Method that adds the songs exp gain to the guest """ 
        self.current_exp += amount
        if self.current_exp >= 100:
            extra_xp = self.current_exp - 100
            self.reset_current_exp()
            self.level_up()
            self.increase_exp(extra_xp)

    def sing_song(self, song):
        """ Method that allow a guest to sing a song """ 
        self.increase_exp(song.xp_gain)
        if self.favourite_song == song.title:
            # BONUS XP :D
            self.increase_exp(song.xp_gain * 0.5)
