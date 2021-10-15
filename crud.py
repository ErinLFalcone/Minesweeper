from model import db, User, Char, Tile, Map, Cont, connect_to_db

def create_user(user_email, user_name, password):
    """Create and return a new user."""

    new_user = User(user_email=user_email,
        user_name=user_name,
        password=password
        )

    db.session.add(new_user)
    db.session.commit()

    return new_user

def create_char(user_id):
    """Create and return a new character."""

    new_char = Char(
        user_id=user_id
        )

    db.session.add(new_char)
    db.session.commit()

    return new_char

def create_map(char_id, map_type):
    """Create and return a new map."""

    new_map = Map(
        char_id=char_id,
        map_type=map_type
        )

    db.session.add(new_map)
    db.session.commit()

    return new_map

def create_tile(x_cord, y_cord, map_id, tile_cont_id=1, is_mutable=True):
    """Create and return a new tile."""

    new_tile = Tile(
        x_cord=x_cord,
        y_cord=y_cord,
        map_id=map_id,
        tile_cont_id=tile_cont_id,
        is_mutable=is_mutable
        )

    db.session.add(new_tile)
    db.session.commit()

    return new_tile

def create_cont(cont_img, is_walkable=True, cont_info=None):
    """Create and return a new map."""

    new_cont = Cont(
        cont_img=cont_img,
        is_walkable=is_walkable,
        cont_info=cont_info
        )

    db.session.add(new_cont)
    db.session.commit()

    return new_cont

def read_user(username):

    user = User.query.filter(
        User.user_name == username
        ).first()

    return user

def read_tile(tile_x, tile_y, map_id=1):

    tile = Tile.query.filter(
        Tile.x_cord == tile_x,
        Tile.y_cord == tile_y,
        Tile.map_id == map_id
        ).first()

    return tile

def move_char(char_id, target_tile):
    """Update character position to a new tile, return new tile."""

    pass