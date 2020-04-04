import datetime

from flask import render_template
from Models.GameClass import Game
from Models.GuessFormClass import GuessForm
from flask import flash
import sys


class MainController:

    def __init__(self):
        # self.stats = self.read_game_stats()
        print()

    def handle_answer(self):
        form = GuessForm()
        form.makeform(self.positions)
        if form.validate_on_submit():
            self.game.validate_guess(form.guess.data)
            if self.game.game_won:
                self.handle_game_win(self.username)
                return render_template('win.jinja')
            return render_template('home.jinja', game=self.game, form=form)
        return render_template('home.jinja', game=self.game, form=form)

    def handle_game_win(self, username):
        file = open("users.txt", "r+")
        with file as f:
            date = str(datetime.datetime.now()).split()[0]
            if username not in f.read():
                file.write("\n" + username + " ")
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
    @property
    def positions(self):
        return self._positions

    @positions.setter
    def positions(self, value):
        self._positions = value

    def new_game(self, numbers, positions, doublenumbers, username):
        self.username = username
        numbers = int(numbers)
        positions = int(positions)
        self.positions = positions
        if str(doublenumbers) == 'on' or positions > numbers:
            doublenumbers = True
        else:
            doublenumbers = False

        form = GuessForm()
        form.makeform(positions)
        self.game = Game(positions, numbers, doublenumbers)
        return render_template('home.jinja', game=self.game, form=form)

    def leaderboard(self):
        file = open('users.txt', 'r')
        user_array = [[]]
        for line in file:
            print(line, file=sys.stderr)
            user_stats = line.split()
            user_stats.append(int((len(user_stats)-1)/2))
            user_array.append(user_stats)

        return render_template('leaderboard.jinja', stats=user_array)
