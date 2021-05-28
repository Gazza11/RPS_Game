from flask import render_template, request
from app import app
from models.game import *
from models.player import Player
from models.player_list import players

@app.route('/')
def index():
    return render_template('index.html', title='Home', players=players)

@app.route('/<input1>/<input2>', methods=['POST'])
def game_r_s(input1, input2):
    player1 = Player('Holder1', input1)
    player2 = Player('Holder2', input2)
    result = Game.game_run(player1, player2)
    return render_template('index.html', title='game')