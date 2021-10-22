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
    crud.fill_new_game()

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

@app.route('/tile_data')
def get_tile_img():
    # import pdb; pdb.set_trace()
 
    tile_x = int(request.args.get("tile_x"))
    tile_y = int(request.args.get("tile_y"))

    tile = crud.read_tile(tile_x, tile_y)
    print(f"tile={tile}")
    
    
    if tile.is_mine:
        
        flash('''Sorry, you lose!\n
            Please try again.''')
        return "F"

    elif tile.mine_count > 0:
        return jsonify([[tile.x_cord, tile.y_cord, tile.mine_count]])

    elif tile.mine_count == 0:
        tile_dict = crud.fill_z_tile_dict(tile)

        js_tile_array = []
         
        for obj, num_mine in tile_dict.items():
            new_list = [obj.x_cord, obj.y_cord, num_mine]
            js_tile_array.append(new_list)

            
        print(jsonify(js_tile_array))

        return jsonify(js_tile_array)

if __name__ == "__main__":
    connect_to_db(app)
    # DebugToolbarExtension(app)
    app.run(host="0.0.0.0", debug=True)
