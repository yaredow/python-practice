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


def computer_guessing_game(x):
    """
    A function that lets the computer guess a number
    """
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        computer_guess = random.randint(low, high)  # Corrected variable name
        feedback = input(
            f"Is {computer_guess} too high (H), too low (L), or correct (C)?? "
        ).lower()
        if feedback == "h":
            high = computer_guess - 1
        elif feedback == "l":
            low = computer_guess + 1

    print(f"Yay, the computer guessed your number, {computer_guess}, correctly!")


guess(10)
