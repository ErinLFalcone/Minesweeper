'''
Database set-up and definitions
'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_email = db.Column(db.String(100), nullable=False, unique=True)
    user_name = db.Column(db.String(16), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return f"<User user_id={self.user_id}, user_email=({self.user_email}), user_name={self.user_name}>"

class Char(db.Model):

    __tablename__ = 'char_data'

    char_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    tile_id = db.Column(db.Integer, db.ForeignKey("tiles.tile_id"))
    char_stuff = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<Char char_id={self.char_id}, user_id=({self.user_id}), (x_cord, y_cord)=({self.x_cord}, ({self.y_cord}), map_id={self.map_id}>"

class Tile(db.Model):
    '''Class for each map tile, with x-coordinate, y-coordinate, map ID, tile contents, and muability'''
    __tablename__ = 'tiles'

    tile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    x_cord = db.Column(db.Integer, nullable=False)
    y_cord = db.Column(db.Integer, nullable=False)
    map_id = db.Column(db.Integer, db.ForeignKey("maps.map_id"))
    tile_content_id = db.Column(db.Integer, db.ForeignKey("tile_cont.tile_cont_id"))
    is_mutable = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Tile tile_id={self.tile_id}, (x_cord, y_cord)=({self.x_cord}, ({self.y_cord}), map_id={self.map_id}>"


class Map(db.Model):

    __tablename__ = 'maps'

    map_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    char_id = db.Column(db.Integer, db.ForeignKey("char_data.char_id"))
    map_type = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return f"<Map map_id={self.map_id}, char_id={self.char_id}, map_type={self.map_type}>"

class Cont(db.Model):

    __tablename__ = 'tile_cont'

    tile_cont_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_walkable = db.Column(db.Boolean, nullable=False)
    content_info = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<Cont tile_cont_id={self.tile_cont_id}, is_walkable={self.is_walkable}>"


def connect_to_db(app):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///fgproject"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)