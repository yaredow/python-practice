"""
random number generator
"""

import random


def guess(x):
    """
    A guessing game where the user tries to guess a random number
    between 1 and x.
    """
    random_number = random.randint(1, x)
    user_guess = 0
    while random_number != user_guess:
        user_guess = int(input(f"Guess number between 1 and {x}: "))
        if user_guess < random_number:
            print("Sorry, guess again. Too low")
        elif user_guess > random_number:
            print("Sorry, guess again. Too high")
    print(f"Yay, congrats. You have guessed the number {random_number}")


guess(10)
