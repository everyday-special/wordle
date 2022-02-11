import argparse

from wordle_ui import ui


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', '-d', action='store_true')
    return parser.parse_args()

def main():
    args = parse_args()
    wordle = ui(debug = args.debug)
    play = True
    while play:
        play = wordle.main()


if __name__ == '__main__':
    main()
