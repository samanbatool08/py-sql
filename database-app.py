from flask importFlask, render_template, request

from cs50 import SQL

app = Flask(__name__)

db  = SQL("sqlite:///froshims.db")

@app.route("/")
def index():
    q = request.args.get("q")
    # can cause SQL injection attack
    # rows = db.execute(f"SELECT * FROM registrants WHERE name = '{q}' ")
    
    # placeholder syntax to sanitize user input
    rows = db.execute("SELECT * FROM registrants WHERE name = :name", name='{q}')
    return render_template("index.html", rows=rows)