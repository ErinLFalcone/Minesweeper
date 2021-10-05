"""Server for farm game!"""

from flask import (Flask, render_template, request, session, redirect)
from model import connect_to_db
import crud

app = Flask(__name__)
app.secret_key = "dev"  # needed for flash and session to work


# Replace this with routes and view functions!
@app.route('/')
def show_index():
    return render_template('base.html')


if __name__ == "__main__":
    connect_to_db(app)
    # DebugToolbarExtension(app)
    app.run(host="0.0.0.0", debug=True)
