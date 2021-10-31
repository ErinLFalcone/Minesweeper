'''
Database set-up and definitions
'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(16), nullable=False, unique=True)
    password = db.Column(db.String(32), nullable=False)
    win_count = db.Column(db.Integer, nullable=False)
    in_game = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"""<User user_id={self.user_id}, 
        username={self.username}>"""

class Tile(db.Model):
    '''Class for each map tile, with x-coordinate, y-coordinate, map ID, tile contents, and muability'''
    __tablename__ = 'tiles'

    tile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    x_cord = db.Column(db.Integer, nullable=False)
    y_cord = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(16), db.ForeignKey("users.username"))
    is_mine = db.Column(db.Boolean, nullable=False)
    mine_count = db.Column(db.Integer, nullable=True)
    is_viewed = db.Column(db.Boolean, nullable=False)
    is_flag = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return (
            f"""<Tile
            tile_id={self.tile_id}, 
            (x_cord, y_cord)=({self.x_cord}, ({self.y_cord})
            >"""
            )


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
