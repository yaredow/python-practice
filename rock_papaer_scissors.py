"""
Module Name: rock_paper_scissors_game

Description:
    This module contains the logic for a simple rock-paper-scissors game
    where the user can play against the computer.

Functions:
    - play: Starts the rock-paper-scissors game.
    - is_win: Determines if the user won based on the game rules.

"""

import random


def play():
    """
    A function that starts the rock, paper, and scissors game.
    """
    while True:
        user = input("'r' for rock, 'p' for paper, and 's' for scissors: ").lower()

        if user not in ["r", "p", "s"]:
            print("Invalid choice! Please choose 'r', 'p', or 's'")
            continue
        computer = random.choice(["r", "p", "s"])

        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie!")
            continue

        if is_win(user, computer):
            print("You won!")
            break

        print("You lost!")
        break


def is_win(player, opponent):
    """
    A function that determines if a user won the game.
    """
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True

    return False


play()
