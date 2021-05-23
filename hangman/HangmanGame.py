import random

class HangmanGame:
    word_list = []

    def __init__(self, word_list):
        self.word_list = word_list

    def play(self):
        hidden_word = random.choice(self.word_list)
        tries = 0

        while tries < 10:

            