from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
chosen_word = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def new_card():
    global flip_timer, chosen_word
    window.after_cancel(flip_timer)
    chosen_word = choice(to_learn)
    language = "French"
    canvas.itemconfig(card_img, image=front_card_img)
    canvas.itemconfig(title, text=language, fill="black")
    canvas.itemconfig(word, text=f"{chosen_word[language]}", fill="black")

    flip_timer = window.after(3000, reverse_card)


def reverse_card():
    language = "English"
    canvas.itemconfig(card_img, image=reverse_card_img)
    canvas.itemconfig(title, text=language, fill="white")
    canvas.itemconfig(word, text=f"{chosen_word[language]}", fill="white")


def remove_word():
    global to_learn
    to_learn.remove(chosen_word)


window = Tk()
window.title("Flash")
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

flip_timer = window.after(1, new_card)

front_card_img = PhotoImage(file="images/card_front.png")
reverse_card_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = canvas.create_image(400, 263, image=front_card_img)
title = canvas.create_text(400, 125, text="Language", font=TITLE_FONT)
word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_btn = Button(image=right_img, highlightthickness=0, command=lambda: [remove_word(), new_card()])
right_btn.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_btn.grid(row=1, column=0)

window.mainloop()

new_df = pd.DataFrame(to_learn)
new_df.to_csv("data/words_to_learn.csv", index=False)
