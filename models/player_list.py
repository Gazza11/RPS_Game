from models.player import Player

player1 = Player('Abed', 'scissors')
player2 = Player('Troy', 'paper')
player3 = Player('Jeff', 'rock')
player4 = Player('Britta', 'scissors')

players = [player1, player2, player3, player4]

def new_players(player1, player2):
    players = []
    players.append(player1)
    players.append(player2)