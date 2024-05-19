import requests
from flask import Flask, render_template

posts_cache = requests.get("https://api.npoint.io/3aedd1c0cd50b79a6a50").json()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", all_posts=posts_cache)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in posts_cache:
        if post['id'] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == '__main__':
    app.run(debug=True)
