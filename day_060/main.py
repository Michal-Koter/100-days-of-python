from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
    if request.method == "POST":
        return f"<h1>Name: {request.form.get('username')}, Password: {request.form.get('password')}</h1>"
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)