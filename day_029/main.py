from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT = ("Arial", 12)


def generate_password():
    letters = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    symbols = ('!', '#', '$', '%', '&', '(', ')', '*', '+')

    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    numbers_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list
    random.shuffle(password_list)
    new_password = "".join(password_list)

    if password_entry.get() != "":
        password_entry.delete(0, END)

    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)


def save_password():
    website = website_entry.get()
    login = login_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "login": login,
            "password": password
        }
    }

    if website == "" or login == "" or password == "":
        messagebox.showerror(title="Oops", message="Pleas make sure you haven't left any fields empty.")
        return None
    else:
        website_entry.delete(0, END)
        login_entry.delete(0, END)
        password_entry.delete(0, END)

        try:
            with open("password.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("password.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("password.json", "w") as file:
                json.dump(data, file, indent=4)


def find_password():
    website = website_entry.get()

    try:
        with open("password.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showerror(title="Error", message=f"No data file found")
    else:
        if website in data:
            login = data[website]["login"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Login: {login}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {website} exists.")




window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=FONT)
website_label.grid(row=1, column=0, sticky=W, padx=10)

website_entry = Entry(width=31)
website_entry.grid(row=1, column=1, sticky=W, pady=5)
website_entry.focus()

search_btn = Button(text="Search", command=find_password, font=("Ariel", 8), width=16)
search_btn.grid(row=1, column=2)

login_label = Label(text="Login:", font=FONT)
login_label.grid(row=2, column=0, sticky=W, padx=10)

login_entry = Entry(width=50)
login_entry.grid(row=2, column=1, columnspan=2, sticky=W, pady=5)

password_label = Label(text="Password:", font=FONT)
password_label.grid(row=3, column=0, sticky=W, padx=10)

password_entry = Entry(width=31)
password_entry.grid(row=3, column=1, sticky=W, pady=5)

generate_pass_btn = Button(text="Generate password", command=generate_password, font=("Ariel", 8), width=16)
generate_pass_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=42, command=save_password)
add_btn.grid(row=4, column=1, columnspan=2, sticky=W, pady=10)

window.mainloop()
