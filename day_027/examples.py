from tkinter import *

window = Tk()
window.title("My First Tkinter Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Ariel", 24))
# my_label.pack(side="left")
my_label.pack()

# my_label["text"] = "New text"
my_label.config(text="New text")

# Button
def button_click():
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_click)
button.pack()

# Entry
input = Entry(width=10)
input.pack()

window.mainloop()