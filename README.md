# Wordle

# Wordle in the terminal, written in python

Simply run `bash run.sh` in your terminal to run. This creates a virtual environment, installs the dependencies, runs wordle.py and then destroys the virtual environment.

To run without immediately destroying the virtual environment:

1. `cd` into the repo
2. `python3 -m venv wordle_venv`
3. `source wordle_venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python3 wordle.py`
