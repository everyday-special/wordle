import os

from secret_word import secretWord
from string import ascii_lowercase
from termcolor import colored

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class gui:
    def __init__(self, allowed_words_file='allowed_guesses.txt'):
        with open(allowed_words_file, 'r') as file:
            self.allowed_words = [line.rstrip() for line in file]
        self.word = secretWord()
        self.letterbank = {}
        self.guesses = []
        for ch in ascii_lowercase:
            self.letterbank.update({ch: 'white'})

    def printGuesses(self):
        clear()
        for guess, colors in self.guesses:
            for i, ch in enumerate(guess):
                self.updateLetterBank(ch, colors[i])
                print(colored(ch, colors[i]), end=' ')
            print()
        self.printLetterBank()

    def updateLetterBank(self, ch, color):

        if (self.letterbank[ch] == 'white' and (color == 'yellow' or color == 'green'))  or (self.letterbank[ch] == 'yellow' and color == 'green'):
            self.letterbank[ch] = color
        elif color == 'white':
            self.letterbank[ch] = 'grey'

    def printLetterBank(self):
        for letter in ascii_lowercase:
            print(colored(letter, self.letterbank[letter]), end=' ')
        print()

    def getInput(self):
        guess = input('Enter your guess: ').lower()
        while guess not in self.allowed_words:
            clear()
            self.printGuesses()
            guess = input('Invalid word. Please enter a valid five letter word: ').lower()
        return guess

    def main(self):
        clear()
        for i in range(6):
            guess = self.getInput()
            colors = self.word.checkGuess(guess)
            self.guesses.append((guess, colors))
            self.printGuesses()
            if colors == ['green'] * 5:
                print("You win!")
                break
        print(f'\n{self.word.word}')
