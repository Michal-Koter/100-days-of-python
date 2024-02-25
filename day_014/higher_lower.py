import os
import random

import art
import game_data


def clear():
    """Clears console screen."""
    # for Windows
    if os.name == 'nt':
        os.system('cls')
    # for Unix
    else:
        os.system('clear')


def show_information(compare: dict, against: dict, score: int):
    """Displays information about game and comparing accounts."""
    clear()
    print(art.logo)
    if score != 0:
        print(f"You're right! Current score: {score}.")

    print(f"Compare A: {compare['name']}, a {compare['description']}, from {compare['country']}.")
    print(art.vs)
    print(f"Against B: {against['name']}, a {against['description']}, from {against['country']}.")


def get_random_account() -> dict:
    """Get data from random account."""
    return random.choice(game_data.data)


def check_answer(compare, against, answer) -> bool:
    """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong."""
    if compare["follower_count"] >= against["follower_count"] and answer == 'a':
        return True
    elif compare["follower_count"] <= against["follower_count"] and answer == 'b':
        return True
    else:
        return False


def start_game():
    """Main game logic."""
    game_should_continue = True
    score = 0

    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        while account_a == account_b:
            account_b = get_random_account()

        show_information(account_a, account_b, score)

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(account_a, account_b, guess)

        if is_correct:
            score += 1
        else:
            game_should_continue = False
            end_game(score)

        account_a = account_b
        account_b = get_random_account()


def end_game(score: int):
    """Print final score."""
    clear()
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {score}")


if __name__ == "__main__":
    start_game()
