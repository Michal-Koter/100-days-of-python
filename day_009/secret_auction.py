import os

import art


def clear():
    # for Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for Unix
    else:
        _ = os.system('clear')


print(art.logo)
print("Welcome to the secret auction program.")

bids = dict()

should_end = False

while not should_end:
    name = input("What is your name?: ")
    price = float(input("What's your bid? $"))
    bids[name] = price

    is_next_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if is_next_bidder == "no":
        should_end = True

    clear()

winner = max(bids)
print(f"The winner is {winner} with a bid of ${bids[winner]}")
