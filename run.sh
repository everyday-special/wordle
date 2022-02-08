#!/bin/bash

python3 -m venv wordle_run_env
source wordle_run_env/bin/activate
pip install -r requirements.txt
python3 wordle.py
deactivate
rm -r wordle_run_env
