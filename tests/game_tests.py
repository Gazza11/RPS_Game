import unittest
from models.player import Player
from models.game import *

class TestGame(unittest.TestCase):
    def setUp(self):

        self.player1 = Player('Abed', 'scissors')
        self.player2 = Player('Troy', 'paper')
        self.player3 = Player('Jeff', 'rock')
        self.player4 = Player('Britta', 'scissors')

        self.game = Game()

#1
    def test_rock_beats_scissors(self):
        self.assertEqual('Jeff wins with rock!', self.game.game_run(self.player3, self.player1))

#2
    def test_scissors_beats_paper(self):
        self.assertEqual('Abed wins with scissors!', self.game.game_run(self.player1, self.player2))

#3
    def test_paper_beats_rock(self):
        self.assertEqual('Troy wins with paper!', self.game.game_run(self.player2, self.player3))

#4
    def test_paper_beats_rock__opposite(self):
        self.assertEqual('Troy wins with paper!', self.game.game_run(self.player3, self.player2))

#5
    def test_scissors_beats_paper__opposite(self):
        self.assertEqual('Abed wins with scissors!', self.game.game_run(self.player2, self.player1))

#6
    def test_rock_beats_scissors__opposite(self):
        self.assertEqual('Jeff wins with rock!', self.game.game_run(self.player1, self.player3))

    def test_draw(self):
        self.assertEqual(None, self.game.game_run(self.player4, self.player1))