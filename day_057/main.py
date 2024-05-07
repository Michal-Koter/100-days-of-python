from flask import Flask, render_template
import requests

from post import Post

posts_cache = []

app = Flask(__name__)


@app.route('/')
def index():
    if not posts_cache:
        get_posts()

    return render_template("main/index.html", posts=posts_cache)


@app.route("/post/<int:num>")
def show_post(num: int):
    if not posts_cache:
        get_posts()

    for post in posts_cache:
        if post.id == num:
            requested_post = post
            break

    return render_template("main/post.html", post=requested_post)


def get_posts():
    global posts_cache

    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response.raise_for_status()

    for post in response.json():
        new_post = Post(post["id"], post["title"], post["subtitle"], post["body"])
        posts_cache.append(new_post)


if __name__ == '__main__':
    app.run(debug=True)
