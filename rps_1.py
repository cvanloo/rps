#!/usr/bin/env python3
import random

TIE = 0
WIN = 1
LOSE = 2

win_table = {}
win_table[("r", "r")] = TIE
win_table[("r", "p")] = LOSE
win_table[("r", "s")] = WIN
win_table[("p", "r")] = WIN
win_table[("p", "p")] = TIE
win_table[("p", "s")] = LOSE
win_table[("s", "r")] = LOSE
win_table[("s", "p")] = WIN
win_table[("s", "s")] = TIE

while True:
    user_move = input("Your move: [r/p/s] ")
    comp_move = ["r", "p", "s"][random.randint(0, 2)]
    print(f"computer plays {comp_move}")
    result = win_table[(user_move, comp_move)]
    print(["It's a tie!", "You won!", "You lost!"][result])
