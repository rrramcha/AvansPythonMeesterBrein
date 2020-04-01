from flask import render_template
from Models.GameClass import Game
from Models.GuessFormClass import GuessForm
from flask import flash

class MainController:
    users = []

    def initialize(self):
        gameFile = open("game.txt", "r")
        gamestate = self.read_gamestate()
        self.game = Game(gamestate)
        # self.stats = self.read_game_stats()
        form = GuessForm()
        if form.validate_on_submit():
            flash('Voer een code in van 4')

        return render_template('home.jinja', stats=gamestate, game=self.game, form=form)

    def read_game_stats(self):
        file = open(".txt", "r")
        data = []
        while 1 < 2:
            line = file.readline()
            print(line)
            if line == "end_stats":
                return data
            else:
                data.append(line.split())

    def read_gamestate(self):
        file = open("game.txt", "r")
        data = []
        while 1 < 2:
            line = file.readline()
            if line == "end_game":
                return data
            else:
                data.append(line)

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        self._game = game
