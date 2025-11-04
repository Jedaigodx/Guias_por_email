from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

# app.run(debug=True)
