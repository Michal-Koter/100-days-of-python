import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for index, row in df.iterrows()}


def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        result = [phonetic_dict[letter] for letter in user_word]
    except KeyError as e:
        print("Sorry, only letters in the alphabet pleas.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()