from flask import render_template, request
from app import app
from models.game import *
from models.player import Player
from models.player_list import *

self = 'self'

@app.route('/')
def index():
    return render_template('welcome.html', title='Home', players=players)

@app.route('/<input_1>/<input_2>', methods=['GET', 'POST'])
def game_r_s(input_1, input_2):
    players[0] = Player('Player 1', input_1)
    players[1] = Player('Player 2', input_2)
    player1 = Player('Player 1', input_1)
    player2 = Player('Player 2', input_2)
    result = Game.game_run(self, player1, player2)
    return render_template('index.html', title='Home', players = players, result=result)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html', title='Welcome')

@app.route('/play')
def play():
    return render_template('index.html', title='play', players=players)