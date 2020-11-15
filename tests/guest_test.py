import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Kakashi Hetaki" , 27, 22.50, "Communications Breakdown")
        self.song    = Song("Aesop Rock", "Lotta Years", 50)
        self.song_2  = Song("Jon Hopkins", "Emerald", 0)
        self.song_3  = Song("Led Zeppelin", "Communications Breakdown", 100)
        self.song_4  = Song("Aesop Rock", "None Shall Pass", 150)

    def test_guest_has_name(self):
        self.assertEqual("Kakashi Hetaki", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(27, self.guest.age)

    def test_guest_has_wallet(self):
        self.assertEqual(22.50, self.guest.wallet)

    def test_guest_can_pay_bill(self):
        self.guest.pay_bill(2.50)
        self.assertEqual(20.00, self.guest.wallet)

    def test_guest_can_increase_xp(self):
        self.guest.increase_exp(50)
        self.assertEqual(50, self.guest.current_exp)

    def test_can_level_up_and_keeps_remaining_xp(self):
        self.guest.increase_exp(150)
        self.assertEqual(50, self.guest.current_exp)
        self.assertEqual(1, self.guest.skill_level)

    def test_can_sing_song(self):
        self.guest.sing_song(self.song)
        self.assertEqual(50, self.guest.current_exp)
    
    def test_bonus_xp(self):
        self.guest.sing_song(self.song_3)
        self.assertEqual(50, self.guest.current_exp)
        self.assertEqual(1, self.guest.skill_level)

    

    