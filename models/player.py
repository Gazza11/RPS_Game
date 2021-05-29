from models.game import *

class Player:
    def __init__(self, name, choice):   
        self.name = name 
        self.choice = choice


    def computer():
        possible_choices = ['rock', 'paper', 'scissors']
        index = random.randint(0,2)
        choice = possible_choices[index]
        computer_file = Player('Computer', choice)
        return computer_file