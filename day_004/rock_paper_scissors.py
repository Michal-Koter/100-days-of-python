import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = ("rock", "paper", "scissors")
game_images = (rock, paper, scissors)

player_chose = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
if 0 <= player_chose <= 2:
    print(game_images[player_chose])
else:
    print("Incorrect choice.")
    exit()

computer_chose = random.randint(0, 2)

print("Computer chose:\n", game_images[computer_chose])

if player_chose == computer_chose:
    print("Draw")
elif (moves[player_chose] == "rock" and moves[computer_chose] == "paper") \
        or (moves[player_chose] == "paper" and moves[computer_chose] == "scissors") \
        or (moves[player_chose] == "scissors" and moves[computer_chose] == "rock"):
    print("You lose")
else:
    print("You win")

