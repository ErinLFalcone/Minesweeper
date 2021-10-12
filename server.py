"""Server for farm game!"""

from flask import (
    Flask, render_template, request, session, redirect, flash
    )
from model import connect_to_db
import crud

app = Flask(__name__)
app.secret_key = "A mystery!"  # needed for flash and session to work


# Replace this with routes and view functions!
@app.route('/')
def show_index():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login():
    
    username = request.form.get("username")
    password = request.form.get("password")

    user = crud.read_user(username)

    try:
        if password == user.password:
            session['username'] = username
            return render_template('base.html')
        else:
            flash('''Username or password incorrect.\n
            Please try again''')
            return redirect('/')
    except:
        flash('''Username or password incorrect.\n
        Please try again''')
        return redirect('/')

if __name__ == "__main__":
    connect_to_db(app)
    # DebugToolbarExtension(app)
    app.run(host="0.0.0.0", debug=True)
