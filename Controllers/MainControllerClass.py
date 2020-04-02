import datetime

from flask import render_template
from Models.GameClass import Game
from Models.GuessFormClass import GuessForm
from flask import flash
import sys


class MainController:

    def __init__(self):
        self.game = Game()
        # self.stats = self.read_game_stats()

    def handle_answer(self):
        form = GuessForm()
        form.makeform(4)
        if form.validate_on_submit():
            self.game.validate_guess(form.guess.data)
            if self.game.game_won:
                self.handle_game_win('Rick')
                return render_template('win.jinja')
            #print(self.game.guess_results[0], file=sys.stderr)
            return render_template('home.jinja', game=self.game, form=form)
        return render_template('home.jinja', game=self.game, form=form)

    def handle_game_win(self, username):
        file = open("users.txt", "r+")
        with file as f:
            date = str(datetime.datetime.now()).split()[0]
            if username not in f.read():
                file.write(username + " ")
            file.write(date + " ")
            file.write(str(len(self.game.guesses)) + " ")

        file.close()

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

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        self._game = game

    def new_game(self):
        form = GuessForm()
        form.makeform(4)
        self.game = Game()
        return render_template('home.jinja', game=self.game, form=form)

