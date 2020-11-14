import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room    = Room(1 , 7.00)
        self.guest   = Guest("Kakashi Hetaki" , 27, 22.50, "Communications Breakdown")
        self.guest_2 = Guest("Asuma Sarutobi", 28, 17.00, "Lotta Years")
        self.guest_3 = Guest("Jiraiya", 51, 47.00, "Brown Eyed Girl")
        self.guest_4 = Guest("Shikamaru Nara", 18, 5.00, "Emerald")
        self.song    = Song("Aesop Rock", "Lotta Years")
        self.song_2  = Song("Jon Hopkins", "Emerald")
        self.song_3  = Song("Led Zeppelin", "Communications Breakdown")


    def test_room_can_add_songs(self):
        self.room.add_song(self.song)
        self.room.add_song(self.song_2)
        list_len = self.room.get_song_list_len()
        self.assertEqual(2, list_len)

    def test_room_can_add_guest(self):
        self.room.add_guest(self.guest)
        self.assertEqual(1, self.room.get_current_guest_list_len())

    def test_if_room_is_full(self):
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest_2)
        self.room.add_guest(self.guest_3)
        is_true = self.room.check_if_room_full()
        self.assertTrue(is_true)

    def test_if_room_is_not_full(self):
        self.room.add_guest(self.guest)
        is_false = self.room.check_if_room_full()
        self.assertFalse(is_false)

    def test_guest_can_pay_bill(self):
        self.assertTrue(self.guest.can_pay_bill(self.room))

    def test_guest_can_not_pay_bill(self):
        self.assertFalse(self.guest_4.can_pay_bill(self.room))

    def test_guest_can_check_in(self):
        self.room.guest_check_in(self.guest)
        self.assertEqual(1, self.room.get_current_guest_list_len())

    def test_room_is_full(self):
        self.room.guest_check_in(self.guest)
        self.room.guest_check_in(self.guest_2)
        self.room.guest_check_in(self.guest_3)
        output = self.room.guest_check_in(self.guest_4)
        self.assertEqual("I'm sorry, this room is currently full, please try another.", output)

    def test_not_enough_funds(self):
        output = self.room.guest_check_in(self.guest_4)
        self.assertEqual("You require more funds.", output)

    def test_get_songs_by_title(self):
        self.room.add_song(self.song)
        self.room.add_song(self.song_2)
        self.room.add_song(self.song_3)
        songs = self.room.get_song_by_title("Emerald")
        self.assertEqual(1, len(songs)) 


    def test_no_songs_found_by_title(self):
        self.room.add_song(self.song_3)
        output = self.room.get_song_by_title("Emerald")
        self.assertEqual("Sorry, we do not have that song", output)

    def test_look_for_fav_song(self):
        self.room.add_song(self.song)
        output = self.guest_2.look_for_fav_song(self.room)
        self.assertEqual("Ya BEAUTY!", output)