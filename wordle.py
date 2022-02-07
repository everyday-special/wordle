"""import os

from secret_word import secretWord
from string import ascii_lowercase
from termcolor import colored

def main():
    guesses = []
    secret_word = secretWord()
    clear()
    for i in range(6):
        guess = input("Enter your guess:\n").lower()
        colors = secret_word.checkGuess(guess)
        guesses.append((guess, colors))
        clear()
        for g in guesses:
            printGuess(g[0], g[1])
        if colors == ['green'] * 5:
            print("\nyou win!")
            break
    print(f'\n{secret_word.word}')


def printGuess(guess, colors):
    for i, ch in enumerate(guess):
        print(colored(ch, colors[i]), end=' ')
    print()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')"""
from wordle_gui import gui

def main():
    wordle_gui = gui()
    wordle_gui.main()


if __name__ == '__main__':
    main()
