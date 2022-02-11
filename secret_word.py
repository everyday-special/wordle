import collections
import random

class secretWord:
    def __init__(self, set_word=None, word_filename='word_list.txt', allowed_guesses_filename='allowed_guesses.txt'):
        with open(word_filename, 'r') as word_file:
            words =  word_file.readlines()
        if set_word is not None:
            self.word = set_word
        else:
            self.word = random.choice(words).rstrip()
        with open(allowed_guesses_filename, 'r') as allowed_guesses:
            self.allowed = set(allowed_guesses.readlines())


    def checkGuess(self, guess):
        counts = collections.Counter(self.word)
        colors = ['white'] * 5
        for i, ch in enumerate(guess):
            if ch == self.word[i]:
                colors[i] = 'green'
                counts[ch] -= 1
                if counts[ch] == 0:
                    counts.pop(ch)
        for i, ch in enumerate(guess):
            if guess[i] in counts and colors[i] != 'green':
                ch = guess[i]
                colors[i] = 'yellow'
                counts[ch] -= 1
                if counts[ch] == 0:
                    counts.pop(ch)
        return colors
