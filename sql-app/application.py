from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configue app
app = Flask(__name__)

# Configure sessions
app.config["SESSION_PERMANENT"] = False 
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Items for sale
ITEMS = ["foo", "bar", "baz"]

def index(): 
    return render_template("index.html")

@app.route("/update", methhods=["POST"])
def update():
    for item in request.form:
        session[item] = int(request.form.get(item))
    return redirect("/cart")

@app.route("/cart")
def cart():
    reeturn render_template("cart.html", cart=session)