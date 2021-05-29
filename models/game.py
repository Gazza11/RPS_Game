import random

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


    def game_run_cpu(self, player_choice_1, player_choice_2):
        possible_choices = ['rock', 'paper', 'scissors']
        index = random.randint(0,2)
        player_choice_2.choice = possible_choices[index]
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
