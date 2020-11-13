import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Kakashi Hetaki" , 27, 22.50)

    def test_guest_has_name(self):
        self.assertEqual("Kakashi Hetaki", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(27, self.guest.age)

    def test_customer_has_wallet(self):
        self.assertEqual(22.50, self.guest.wallet)