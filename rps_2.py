#!/usr/bin/env python3
import random

while True:
    user_move_str = input("Your move: [r/p/s] ")
    user_move = ["r", "p", "s"].index(user_move_str) + 1

    comp_move = random.randint(1, 3)
    comp_move_str = ["r", "p", "s"][comp_move - 1]

    print(f"computer plays {comp_move_str}")
    print(["It's a tie!", "You won!", "You lost!"][(user_move - comp_move) % 3])
