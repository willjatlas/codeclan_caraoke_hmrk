import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room()
        self.guest = Guest("Kakashi Hetaki" , 27, 22.50)
        self.guest_2 = Guest("Asuma Sarutobi", 28, 17.00)
        self.song = Song("Aesop Rock", "Lotta Years")
        self.song_2 = Song("Jon Hopkins", "Emerald")

    def test_room_has_songs(self):
        self.room.add_song(self.song)
        self.room.add_song(self.song_2)
        list_len = self.room.get_song_list_len()
        self.assertEqual(2, list_len)

    def test_room_has_guests(self):
        self.room.add_guest(self.guest)
        self.room.add_guest(self.guest_2)
        
