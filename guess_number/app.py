import random

def guess(x):
    secret_number = random.randint(1, x)
    limit = 3
    tries = 0
    won = False

    while tries < limit and not(won):
        user_number = int(input(f"Guess a number between 1 and {x}: "))
        won = secret_number == user_number
        tries += 1

        if user_number < secret_number:
            print("The secret number is greater.")
        elif user_number > secret_number:
            print("The secret number is lower.")

    if won:
        print("You win!")
    else:
        print("You lose.")

def computer_guess(x):
    min = 1
    max = x
    limit = 3
    tries = 0
    feedback = ""
    won = False

    while tries < limit and not(won):
        print("Computer, guess the number please!")
        computer_number = random.randint(min, max)
        feedback = input(f"Is {computer_number} correct? ")

        if feedback == "correct":
            won = True
        elif feedback == "higher":
            min = computer_number + 1
        elif feedback == "lower":
            max = computer_number - 1

        tries += 1

    if won:
        print("Computer wins!")
    else:
        print("Computer loses.")

computer_guess(10)
