import unittest
from models.player import Player

from models.game import *

class TestPlayer(unittest.TestCase):
    def setUp(self):

        self.player1 = Player('Abed', 'scissors')

    def test_player_name(self):
        self.assertEqual('Abed', self.player1.name)

    def test_player_choice(self):
        self.assertEqual('scissors', self.player1.choice)