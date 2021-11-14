from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

#Our User database.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    posts = db.relationship('Post', backref='user', passive_deletes='True') #one to many relationship


#Posts model
class Post(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    text =db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False) #making sure the integer is matching a real user in the database.
    