import os

from secret_word import secretWord
from string import ascii_lowercase
from termcolor import colored

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class ui:
    def __init__(self, allowed_words_file='allowed_guesses.txt'):
        with open(allowed_words_file, 'r') as file:
            self.allowed_words = [line.rstrip() for line in file]
        self.letterbank = {}
        self.scores = []

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
        elif color == 'white' and self.letterbank[ch] == 'white':
            self.letterbank[ch] = 'grey'

    def printLetterBank(self):
        for letter in ascii_lowercase:
            print(colored(letter, self.letterbank[letter]), end=' ')
        print()

    def getGuess(self):
        guess = input('Enter your guess: ').lower()
        while guess not in self.allowed_words:
            clear()
            self.printGuesses()
            guess = input('Invalid word. Please enter a valid five letter word: ').lower()
        return guess

    def playAgain(self):
        response = input('Do you want to play again? (y/n): ')
        while response not in 'yn':
            response = input('Please enter "y" or "n" to indicate whether you want to play again: ')
        if response == 'n':
            self.printScores()
        return response == 'y'

    def reset(self):
        self.word = secretWord()
        self.guesses = []
        for ch in ascii_lowercase:
            self.letterbank.update({ch: 'white'})

    def printScores(self):
        for score in self.scores:
            print(f'{score[0]}: {score[1]}/6')

    def main(self):
        score = None
        self.reset()
        clear()
        win = False
        for i in range(1, 7):
            guess = self.getGuess()
            colors = self.word.checkGuess(guess)
            self.guesses.append((guess, colors))
            self.printGuesses()
            if colors == ['green'] * 5:
                print("You win!")
                win = True
                score = i
                break
        if not score:
            score = '-'
        self.scores.append((self.word.word, score))
        if not win:
            print(f'\nThe word was "{self.word.word}"')
        return self.playAgain()
