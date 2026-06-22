# ----------------------------------------
# CODSOFT Python Programming Internship
# Task 4: Rock Paper Scissors Game
#
# Description:
# This is a simple Rock-Paper-Scissors game where
# the user plays against the computer.
# The program uses random selection, conditional
# statements, and user input.
#
# Developed by: Devyani Verma
# ----------------------------------------

import random

choices = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Enter Rock, Paper, or Scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(choices)

    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You Win! 🎉")

    else:
        print("Computer Wins! 🤖")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break