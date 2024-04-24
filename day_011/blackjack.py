import os
import random

import art

DECK_NUM = 2
COLOR_NUM = 4


def clear():
    # for Windows
    if os.name == 'nt':
        os.system('cls')
    # for Unix
    else:
        os.system('clear')


def check(cards):
    points = sum(cards)

    aces = cards.count(11)

    for i in range(aces):
        if points > 21:
            points -= 10

    return points


def player_draw(player_cards, dealer_card):
    if check(player_cards) >= 21:
        return None

    print(f"Your cards: {player_cards}, current score: {check(player_cards)}")
    print(f"Dealer's first card: {dealer_card}")

    another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if another == 'y':
        player_cards.append(
            deck.pop(random.randint(0, len(deck) - 1)))
        player_draw(player_cards, dealer_card)


def dealer_draw(cards):
    if check(cards) < 17:
        cards.append(
            deck.pop(random.randint(0, len(deck) - 1))
        )
        dealer_draw(cards)


def game():
    player_cards, dealer_cards = [], []

    player_cards.append(
        deck.pop(random.randint(0, len(deck) - 1)))
    dealer_cards.append(
        deck.pop(random.randint(0, len(deck) - 1)))

    player_cards.append(
        deck.pop(random.randint(0, len(deck) - 1)))
    dealer_cards.append(
        deck.pop(random.randint(0, len(deck) - 1)))

    if check(player_cards) == 21:
        print("Blackjack!")
        if check(dealer_cards) != 21:
            print("You won!")
        else:
            print("Draw!")
        return None

    player_draw(player_cards, dealer_cards[0])
    player_score = check(player_cards)

    if player_score > 21:
        print(f"Your cards : {player_cards}, current score: {player_score}")
        print(f"Dealer's cards : {dealer_cards}, current score: {check(dealer_cards)}")
        print("You lose!")
        return None

    dealer_draw(dealer_cards)
    dealer_score = check(dealer_cards)

    print(f"Your cards : {player_cards}, current score: {player_score}")
    print(f"Dealer's cards : {dealer_cards}, current score: {dealer_score}")

    if player_score == dealer_score:
        print("Draw!")
    elif dealer_score > 21 or dealer_score < player_score:
        print("You win")
    else:
        print("You lose!")


def play_on():
    play = input("Do you want to play a game Blackjack? 'y' for yes, 'n' for no: ").lower()
    return play == 'y'


while play_on():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * COLOR_NUM * DECK_NUM
    random.shuffle(deck)

    clear()
    print(art.logo)

    game()
