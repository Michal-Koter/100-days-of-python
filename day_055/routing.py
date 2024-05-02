from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper


def make_underline(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper


@app.route('/')
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is paragraph.</p>'
            '<img src="https://media.giphy.com/media/gKHGnB1ml0moQdjhEJ/giphy.gif?cid=82a1493bycadq4p9yjqxl2krdxgle1anuk1kn1d911q59mrf&ep=v1_gifs_trending&rid=giphy.gif&ct=g" width-250>')


@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return 'Bye!'


@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'


if __name__ == '__main__':
    app.run(debug=True)
