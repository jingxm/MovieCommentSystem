# coding:utf-8
from . import db, login_manager, app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import sys

#电影类，具有的属性包括电影名字、导演、简介、演员、图片、上映日期、豆瓣评分

class Movie(db.Model):
    __searchable__ = ['name', 'actor', 'director']
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    director = db.Column(db.String(200))
    summary = db.Column(db.Text)
    actor = db.Column(db.String(200))
    image = db.Column(db.String(164))
    date = db.Column(db.String(200))
    url = db.Column(db.String(200))
    rating = db.Column(db.Float)
    
    def __repr__(self):
        return "This movie is %r" % self.name
