PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt", "r") as letter:
    content = letter.read()

if content == "":
    print("No letters")
    exit(1)

with open("Input/Names/invited_names.txt", "r") as invited:
    names = invited.readlines()

for name in names:
    name = name.strip()
    new_mail = content.replace(PLACEHOLDER, str(name))
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        file.write(new_mail)
