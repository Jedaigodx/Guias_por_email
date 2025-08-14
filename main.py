from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def user():
    return render_template("user.html")

app.run(debug=True)