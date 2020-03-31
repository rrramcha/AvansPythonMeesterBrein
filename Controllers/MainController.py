import random

from flask import render_template


class MainController:

    users = []

    def initialize(self):
        usersFile = open('users.txt', 'r')
        while 1 < 2:
            line = usersFile.readline()


        self.stats = self.read_game_stats(username)
        self.gamestate = self.read_gamestate(username)
        return render_template('home.jinja', stats=self.stats)

    def read_game_stats(self, username):
        file = open(username + ".txt", "r")
        data = []
        while 1 < 2:
            line = file.readline()
            print(line)
            if line == "end_stats":
                return data
            else:
                data.append(line.split())

    def read_gamestate(self, username):
        file = open(username + ".txt", "r")
        data = []


