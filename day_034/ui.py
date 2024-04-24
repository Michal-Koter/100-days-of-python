from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizWindow:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.geometry("400x550")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Ariel", 12))
        self.score.grid(row=0, column=1, padx=20, pady=20, sticky=E)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, width=280, text="Question", font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky=N)

        self.tick_img = PhotoImage(file="images/true.png")
        self.tick_btn = Button(image=self.tick_img, highlightthickness=0, bg=THEME_COLOR, command=self.tick_clicked)
        self.tick_btn.grid(row=2, column=0, padx=20, pady=20, sticky=W)

        self.cross_img = PhotoImage(file="images/false.png")
        self.cross_btn = Button(image=self.cross_img, highlightthickness=0, bg=THEME_COLOR, command=self.cross_clicked)
        self.cross_btn.grid(row=2, column=1, padx=20, pady=20, sticky=E)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()

            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reach the end of the quiz.")
            self.tick_btn.config(state="disabled")
            self.cross_btn.config(state="disabled")

    def tick_clicked(self):
        is_correct = self.quiz_brain.check_answer("True")
        self.give_feedback(is_correct)

    def cross_clicked(self):
        is_correct = self.quiz_brain.check_answer("False")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct: bool):
        score = self.quiz_brain.score
        self.score.config(text=f"Score: {score}")

        self.canvas.config(bg="green" if is_correct else "red")
        self.window.after(1000, self.get_next_question)