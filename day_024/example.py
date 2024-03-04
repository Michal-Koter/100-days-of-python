# # Fist way to open file
# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

# Second way to open file
with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)

with open("my_file.txt", "w") as file:
    file.write("New text.")

with open("my_file.txt", "a") as file:
    file.write("\nNext text.")

with open("new_file.txt", "w") as file:
    file.write("New text file.")
