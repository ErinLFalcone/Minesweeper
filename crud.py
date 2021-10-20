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

def adj_mine_setter(num_tile, mine_list):
    
    for i in range(1,num_tile+1):
        if i not in mine_list:
            tile_mine_count = 0
            not_mine = Tile.query.filter_by(tile_id=i).first()
            nm_x = not_mine.x_cord
            nm_y = not_mine.y_cord

            check_x_cord = nm_x-1
            while check_x_cord <= nm_x+1:
                check_y_cord = nm_y-1
                while check_y_cord <= nm_y+1:
                    check_tile = Tile.query.filter_by(
                        x_cord=check_x_cord, y_cord=check_y_cord
                        ).first()
                    try:
                        if check_tile.is_mine == True:
                            tile_mine_count+=1
                    except:
                        pass
                    check_y_cord +=1
                check_x_cord +=1

            setattr(not_mine, 'mine_count', tile_mine_count)
            db.session.commit()


def fill_new_game(num_mine=20):

    last_tile = Tile.query.order_by(Tile.tile_id.desc()).first()

    num_tile = last_tile.tile_id

    mine_list = r.sample(range(1,num_tile+1), num_mine)

    # mine_list = [1,22]

    for mine in mine_list:
        mine_tile = Tile.query.filter_by(tile_id=mine).first()
        setattr(mine_tile, 'is_mine', True)
        db.session.commit()
            
    adj_mine_setter(num_tile, mine_list)

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