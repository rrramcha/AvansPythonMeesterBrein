import random
import sys


class Game:

    def __init__(self, positions, numbers, doublenumbers):
        code = []
        self.guesses = []
        self.guess_results = []
        print(doublenumbers, file=sys.stderr)
        for i in range(positions):
            random_num = random.randint(1, numbers)
            if not doublenumbers:
                while random_num in code:
                    random_num = random.randint(1, numbers)
            code.append(random_num)
        self.code = code
        self.game_won = False

    def validate_guess(self, guess):
        correct_guesses = []
        temp_code = self.code.copy()
        if guess is not None:
            for i in range(len(guess)):
                if int(guess[i]) == temp_code[i]:
                    temp_code[i] = None
                    correct_guesses.append(1)
                elif int(guess[i]) in temp_code:
                    temp_code[temp_code.index(int(guess[i]))] = None
                    correct_guesses.append(2)
                else:
                    correct_guesses.append(3)
            self.game_won = all(number is 1 for number in correct_guesses)

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

    @property
    def game_won(self):
        return self._game_won

    @game_won.setter
    def game_won(self, value):
        self._game_won = value
