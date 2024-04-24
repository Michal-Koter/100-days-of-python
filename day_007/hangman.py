import random
import hangman_arts
from hangman_words import word_list

end_of_game = False
left_tries = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
blanked_word = ["_"] * word_length

print(hangman_arts.logo)

while not end_of_game:
    letter = input("Guess a letter: ").lower()

    if letter in blanked_word:
        print(f"You've already guessed {letter}\n")

    for i in range(word_length):
        if letter == chosen_word[i]:
            blanked_word[i] = letter

    if letter not in chosen_word:
        print(f"You guessed {letter}, that's not in the word. You lose a life.\n")

        left_tries -= 1
        if left_tries == 0:
            end_of_game = True
            print("You lose.\n")

    print("".join(blanked_word))

    if "_" not in blanked_word:
        end_of_game = True
        print("You win.\n")

    print(hangman_arts.stages[left_tries])

print(f"Guessing word: {chosen_word}")
