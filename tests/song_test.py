import unittest

from src.song import Song 

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Aesop Rock", "Lotta Years", 50)

    def test_song_had_artist(self):
        self.assertEqual("Aesop Rock", self.song.artist)

    def test_song_has_title(self):
        self.assertEqual("Lotta Years", self.song.title)
    
    def test_song_has_xp(self):
        self.assertEqual(50, self.song.xp_gain)
        