from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def index():
    year = datetime.now().year
    return render_template("examples/index.html", year=year)

@app.route('/guess/<name>')
def guess(name):
    params = {"name": name}

    response = requests.get("https://api.agify.io", params=params)
    response.raise_for_status()
    age = response.json()["age"]

    response = requests.get("https://api.genderize.io", params=params)
    response.raise_for_status()
    gender = response.json()["gender"]

    name = name.title()
    return render_template("examples/guess.html", name=name, age=age, gender=gender)

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response.raise_for_status()
    posts = response.json()

    return render_template("examples/blog.html", posts=posts)


if __name__ == '__main__':
    app.run(debug=True)