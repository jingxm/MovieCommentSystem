# coding:utf-8
from . import db, login_manager, app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import sys

#电影类，具有的属性包括电影名字、导演、简介、演员、图片、上映日期、豆瓣评分、烂番茄评分、IMDb评分
#其中每个电影会与若干个评论相关
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
    imdb_rating = db.Column(db.Float)
    tomato_rating = db.Column(db.Integer)
    imdb_url = db.Column(db.String(200))
    comment = db.relationship('Comment', backref="Movie", lazy="dynamic")

    #如果不存在烂番茄评分，返回-1.存在则返回评分以及百分比符号
    def ret_tomato(self):
        if self.tomato_rating == -1:
            return -1
        else:
            return str(self.tomato_rating)+'%'
    def __repr__(self):
        return "This movie is %r" % self.name

#用户类，包括用户名、密码、邮箱、电话、评论，其中每名用户会有若干评论。
class User(db.Model, UserMixin):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(200))
    password_hash = db.Column(db.String(200))
    email = db.Column(db.String(200))
    phone = db.Column(db.String(100))
    comment = db.relationship('Comment', backref="User", lazy="dynamic")

    #注册callback，借此登录用户
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    #简单的异常处理
    @property
    def password(self):
        raise AttributeError('读取密码发生错误！')

    #注册时将密码转为带盐哈希存储
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    #登录时验证密码
    def password_verification(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "This user is %r" % self.username

#电影评论类，具有标题、内容、评分、日期的属性，每个评论关联用户、电影。
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    rating = db.Column(db.Float)
    movie_id = db.Column(db.Integer, db.ForeignKey(Movie.id))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    date = db.Column(db.String(200))
    
    def __repr__(self):
        return "This comment is %r" % self.title

    #返回此评论的用户名称
    def to_user(self):
        return self.User.username

    #返回此评论关联的电影名称
    def to_movie(self):
        return self.Movie.name

    #返回评论你关联的电影海报
    def to_image(self):
        return self.Movie.image

    #返回此评论的评分
    def percentige(self):
        return self.rating*10

'''
#帖子类，待用
class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text)
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer, db.ForeignKey(Movie.id))
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    date = db.Column(db.DateTime)
    def __repr__(self):
        return "This post is %r" % self.title
'''