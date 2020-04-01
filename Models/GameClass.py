import random
import sys


class Game:
    def __init__(self, guesses):
        print(guesses, file=sys.stderr)
        if guesses[0] is None:
            self.make_new_game()
        else:
            self.code = guesses[0]
            self.guesses = guesses[1:]

    def make_new_game(self):
        code = []
        for i in range(4):
            randomNum = random.randint(1, 9)
            while randomNum in code:
                randomNum = random.randint(1, 9)
            code.append(randomNum)
        self.code = code

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def guesses(self):
        return self._guesses

    @guesses.setter
    def guesses(self, guesses):
        self._guesses = guesses
