from flask import render_template, request
from app import app
from models.game import Game
from models.player import Player

@app.route('/game')
def index():
    return render_template('index.html', title='Home')