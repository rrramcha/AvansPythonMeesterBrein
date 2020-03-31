import random

from flask import render_template


class GameController:

    def __init__(self):
        self.code = []

    def game_start(self):
        username = 'Rick'
        try:
            code = open(username + ".txt", "r")
        except IOError:
            code = open(username + ".txt", "w+")
        self.code = code.read()
        if username in self.code:
            return render_template('home.jinja', code=self.code)
        return render_template('home.jinja', code=self.code)

    def read_game_stats(self, username):
        file = open(username + ".txt", "r")
        line = ""
        isStats = True
        while isStats:
            line = file.readline()
            if line is "end_stats":
                isStats = False
            else:
                data = line.split()


