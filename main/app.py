
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/players")
def players():
    return render_template("players.html")

if __name__ == "__main__":
    app.run()
