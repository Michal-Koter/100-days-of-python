from tkinter import *

FONT = ("Arial", 16)


def miles_to_km():
    miles = float(entry.get())
    kilometers = round(miles * 1.609344, 2)
    result.config(text=kilometers)

window = Tk()
window.title("Km to Mile Converter")
window.geometry("300x200")
window.config(padx=30, pady=50)

miles = Label(text="Miles", font=FONT)
miles.grid(row=0, column=3)

km = Label(text="Km", font=FONT)
km.grid(row=1, column=3)

equal = Label(text="is equal to", font=FONT)
equal.grid(row=1, column=0)

result = Label(text="0", font=FONT)
result.grid(row=1, column=1)

submit = Button(text="Convert", font=("Ariel", 12), command=miles_to_km)
submit.grid(row=2, column=1)

entry = Entry(width=10)
entry.grid(row=0, column=1)


window.mainloop()
