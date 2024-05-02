from flask import Flask
import random

app = Flask(__name__)
guessing_number = random.randint(0, 9)


@app.route('/')
def index():

    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYmZ2bGVid3l0ODY2dTc2ZHZlZ3E3bnE0eXE5emxib3pzcnVyc2F1NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hTrCbhPoQEcCT18JLf/giphy.gif" width="480" height="270">')


@app.route('/<int:number>')
def guess_number(number):
    if number == guessing_number:
        body = ('<h1 style="color: green">You found me!</h1>'
                '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWJtZDI1NzlzMDBhM3pjY2s3bXlpdnhzcjB6enNjc3RtYnd3MXMxaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/elsol3P5Jt2ASsxLva/giphy.gif" width="480" height="480">')
    elif number > guessing_number:
        body = ('<h1 style="color: purple">Too high try again!</h1>'
                '<img src="https://i.giphy.com/3o6ZtaO9BZHcOjmErm.webp" width="480" height="480">')
    else:
        body = ('<h1 style="color: red">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="480" height="480">')

    return body


if __name__ == '__main__':
    app.run(debug=True)

