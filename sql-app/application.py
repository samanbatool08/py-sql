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

