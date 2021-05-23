import random

def play():
    # -1 = lose, 0 = draw, 1 = win
    rules = {
        "r": {
            "r": "tie",
            "s": "win",
            "p": "lose"
        },
        "s": {
            "r": "lose",
            "s": "tie",
            "p": "win"
        },
        "p": {
            "r": "win",
            "s": "lose",
            "p": "tie"
        }
    }

    result = "tie"

    while (result == "tie"):
        user_move = input("Rock (r), scissors (s) or paper (p)? ")
        computer_move = random.choice(list(rules.keys()))
        print(f"Computer: {computer_move}")
        result = rules[user_move][computer_move]

    if (result == "win"):
        print("You win!")
    elif (result == "lose"):
        print("You lose.")

play()