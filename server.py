"""Server for farm game!"""

from flask import (
    Flask, render_template, request, session, redirect, flash, jsonify
    )
from model import connect_to_db
import crud

app = Flask(__name__)
app.secret_key = "A mystery!"  # needed for flash and session to work

@app.route('/')
def show_index():

    try:
        if session['logged'] == True:
            if crud.read_user(session['username']).in_game:
                return render_template('game.html')
            win_count = crud.read_user(session['username']).win_count
            return render_template('int.html', win_count=win_count)
    except KeyError:
            return render_template('login.html')

@app.route('/login', methods=["POST"])
def login():
    
    username = request.form.get("username")
    password = request.form.get("password")

    user = crud.read_user(username)

    try:
        if password == user.password:
            session['logged'] = True
            session['username'] = username
            return redirect('/')
        else:
            flash('''Username or password incorrect.\n
            Please try again''')
            return redirect('/')
    except:
        flash('''Username or password incorrect.\n
        Please try again''')
        return redirect('/')

@app.route('/create_account')
def create_account():
    try:
        if session['logged'] is True:
            redirect('/')
    except KeyError:
        return render_template('create_account.html')

@app.route('/try_account', methods=["POST"])
def try_account():

    username = request.form.get("new_username")
    password = request.form.get("new_password")

    if crud.read_user(username) is None:
        crud.create_user(username, password)
        print(crud.read_user(username))
        session['logged'] = True
        session['username'] = username
        return redirect('/')
    else:
        flash('''Sorry, that username is taken.\n
            Please try again''')
        return redirect('/create_account')

@app.route('/minesweeper')
def minesweeper():
    try:
        if session['logged'] == True:
            crud.set_in_game(session['username'])
            crud.fill_new_game(session['username'])
            return render_template('game.html')
    except KeyError:
            return render_template('login.html')

@app.route('/win_lose')
def win_lose():

    win_state = request.args.get("win_state")

    if win_state == 'win':
        crud.increment_wins(session['username'])

    crud.set_not_in_game(session['username'])

    return "OK"

@app.route('/read_viewed_tiles')
def read_viewed_tiles():

    return jsonify(crud.read_viewed_tiles(session['username']))

@app.route('/tile_data')
def get_tile_data():
    # import pdb; pdb.set_trace()
 
    tile_x = int(request.args.get("tile_x"))
    tile_y = int(request.args.get("tile_y"))
    flag = request.args.get("flag")

    if flag == "True":
        flag = True
    elif flag == "False":
        flag = False

    if flag:
        tile_to_flag = crud.read_tile(tile_x, tile_y, session['username'])
        crud.flag_tile(tile_to_flag)
        return "OK"

    tile = crud.read_tile(tile_x, tile_y, session['username'])
   
    if tile.is_mine:
       
        return jsonify([[tile.x_cord, tile.y_cord, '💥']])

    elif tile.mine_count > 0:
        return jsonify([[tile.x_cord, tile.y_cord, tile.mine_count]])

    elif tile.mine_count == 0:
        tile_dict = crud.fill_z_tile_dict(tile, session['username'])

        js_tile_array = []
         
        for obj, num_mine in tile_dict.items():
            new_list = [obj.x_cord, obj.y_cord, num_mine]
            js_tile_array.append(new_list)

        return jsonify(js_tile_array)

@app.route('/all_mines')
def get_all_mines():

    print("mine request to server")

    all_mines = []

    for mine in crud.read_all_mines(session['username']):
        mine_cords = [
            mine.x_cord,
            mine.y_cord
        ]
        all_mines.append(mine_cords)

    return jsonify(all_mines)

if __name__ == "__main__":
    connect_to_db(app)
    # DebugToolbarExtension(app)
    app.run(host="0.0.0.0", debug=True)
