import random
import sys

class Game:

    def __init__(self):
        code = []
        self.guesses = [[]]
        self.guess_results = [[]]
        for i in range(4):
            random_num = random.randint(1, 9)
            while random_num in code:
                random_num = random.randint(1, 9)
            code.append(random_num)
        self.code = code

    def validate_guess(self, guess):
        correct_guesses = []

        for i in range(len(guess)):
            if int(guess[i]) == self.code[i]:
                correct_guesses.append(1)
            elif int(guess[i]) in self.code:
                correct_guesses.append(2)
            else:
                correct_guesses.append(3)

        random.shuffle(correct_guesses)
        self.add_guess_result(correct_guesses)
        self.add_guess(guess)

    @property
    def guess_results(self):
        return self._guess_results

    @guess_results.setter
    def guess_results(self, guess_results):
        self._guess_results = guess_results

    def add_guess_result(self, result):
        self._guess_results.append(result)

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

    def add_guess(self, guess):
        self._guesses.append(guess)
