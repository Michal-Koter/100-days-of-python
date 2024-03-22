from ui import QuizWindow
from question_model import Question
from quiz_brain import QuizBrain
import requests

params = {
    "amount": 10,
    "difficulty": "hard",
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=params)
response.raise_for_status()
data = response.json()["results"]

question_bank = []
for question in data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizWindow(quiz)