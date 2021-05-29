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
def play_hold():
    return render_template('play.html', title='Play', players=players)

@app.route('/play', methods=['POST'])
def play():
    player1_name = request.form["player1-name"]
    player2_name = request.form['player2-name']
    player1_choice = request.form['player1-choice']
    player2_choice = request.form['player2-choice']
    players[0] = Player(player1_name, player1_choice)
    players[1] = Player(player2_name, player2_choice)
    player1 = Player(player1_name, player1_choice)
    player2 = Player(player2_name, player2_choice)
    result = Game.game_run(self, player1, player2)
    return render_template('index.html', title='play', players=players, result=result)


@app.route('/play-cpu')
def cpu_hold():
    return render_template('cpu.html', title='Play the CPU')

@app.route('/play-cpu', methods=['POST'])
def play_cpu():
    computer = Player.computer()
    player1_name = request.form["player1-name"]
    player1_choice = request.form['player1-choice']
    players[0] = Player(player1_name, player1_choice)
    players[1] = computer
    player1 = Player(player1_name, player1_choice)
    player2 = computer
    result = Game.game_run(self, player1, player2)
    return render_template('index.html', title='play', players=players, result=result)
