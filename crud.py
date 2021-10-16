from model import db, User, Tile, connect_to_db
import random as r

def create_user(user_email, user_name, password):
    """Create and return a new user."""

    new_user = User(user_email=user_email,
        user_name=user_name,
        password=password
        )

    db.session.add(new_user)
    db.session.commit()

    return new_user

def create_tile(x_cord, y_cord, is_mine=False, mine_count=0):
    """Create and return a new tile."""

    new_tile = Tile(
        x_cord=x_cord,
        y_cord=y_cord,
        is_mine=is_mine,
        mine_count=mine_count        
        )

    db.session.add(new_tile)
    db.session.commit()

    return new_tile

def fill_new_game(num_mine=20):

    last_tile = Tile.query.order_by(Tile.tile_id.desc()).first()

    num_tile = last_tile.tile_id

    mine_list = r.sample(range(num_tile), num_mine)

    for mine in mine_list:
        mine_tile = Tile.query.filter_by(tile_id=mine).first()
        # mine_tile.update().values(is_mine=True)
        setattr(mine_tile, 'is_mine', True)

    return mine_list

def read_user(username):

    user = User.query.filter(
        User.user_name == username
        ).first()

    return user

def read_tile(tile_x, tile_y):

    tile = Tile.query.filter(
        Tile.x_cord == tile_x,
        Tile.y_cord == tile_y
        ).first()

    return tile