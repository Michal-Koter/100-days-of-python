class QuizBrain:
    def __init__(self, questions):
        self.question_num = 0
        self.question_list = questions
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self) -> bool:
        return self.question_num < len(self.question_list)

    def check_answer(self, user_answer, correct_answer) -> bool:
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_num}\n")
