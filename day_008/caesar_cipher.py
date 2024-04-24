import art

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


def caesar_cipher(text, shift, direction):
    new_text = ""
    alphabet_len = len(alphabet)

    if direction == "decode":
        shift *= -1

    for char in text:
        if char.isalpha():
            position = (alphabet.index(char) + shift) % alphabet_len
            new_text += alphabet[position]
        else:
            new_text += char

    print(f"The {direction} text is: {new_text}")


print(art.logo)

should_end = False

while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if restart == "no":
        should_end = True
        print("Goodbye")
