from wordle_ui import ui

def main():
    wordle = ui()
    play = True
    while play:
        play = wordle.main()


if __name__ == '__main__':
    main()
