class Game:
    def __init__(self):
        pass
    
    def game_run(self, player_choice_1, player_choice_2):
        if player_choice_1.choice == player_choice_2.choice:
            return None
        elif player_choice_1.choice == 'rock' and player_choice_2.choice == 'scissors':
            return f'{player_choice_1.name} wins with {player_choice_1.choice}!'
        elif player_choice_1.choice == 'scissors' and player_choice_2.choice == 'paper':
            return f'{player_choice_1.name} wins with {player_choice_1.choice}!'
        elif player_choice_1.choice == 'paper' and player_choice_2.choice == 'rock':
            return f'{player_choice_1.name} wins with {player_choice_1.choice}!'
        else:
            return f'{player_choice_2.name} wins with {player_choice_2.choice}!'


    # def new_players(self, player1, player2):
    #     players = []
    #     players.append(player1)
    #     players.append(player2)
    #     # return players
