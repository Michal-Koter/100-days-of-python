import requests
from flask import Flask, render_template, request
import smtplib
import os

OWN_EMAIL = os.environ.get('EMAIL')
OWN_PASSWORD = os.environ.get('EMAIL_PASS')

posts_cache = requests.get("https://api.npoint.io/3aedd1c0cd50b79a6a50").json()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", all_posts=posts_cache)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        sender_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for post in posts_cache:
        if post['id'] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)

def sender_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

if __name__ == '__main__':
    app.run(debug=True)
