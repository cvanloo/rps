import random

while True:
    user_move = ["r", "p", "s"].index(input("Your move: [r/p/s] ")) + 1
    comp_move = random.randint(1, 3)
    print(f"Computer plays {['r', 'p', 's'][comp_move - 1]}")
    print(["It's a tie!", "You won!", "You lost!"][(user_move - comp_move) % 3])
