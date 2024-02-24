import os
import random

import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def clear():
    # for Windows
    if os.name == 'nt':
        os.system('cls')
    # for Unix
    else:
        os.system('clear')


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        turns -= 1
    elif guess < answer:
        print("Too low.")
        turns -= 1
    else:
        print(f"You got it! The answer was {answer}.")

    return turns


def set_difficulty():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            return EASY_LEVEL_TURNS
        elif difficulty == "hard":
            return HARD_LEVEL_TURNS

        print("Wrong difficulty. Try again.")


def game():
    clear()
    print(art.logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    turns = set_difficulty()
    guess = None

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The answer was {answer}")
            return


if __name__ == "__main__":
    game()
