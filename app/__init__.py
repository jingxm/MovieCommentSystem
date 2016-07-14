#-*-coding:utf-8-*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#新建Flask实例，对该实例进行参数设置
app = Flask(__name__)
app.config['SECRET_KEY'] = "You guess"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///D:/AAAA/CODE/data.sqlite"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['WHOOSH_BASE'] = "search.db"
app.config['MAX_SEARCH_RESULTS'] = 100
app.config['UPLOAD_FOLDER'] = 'app/static/image/'

#创建SQLALchemy对象
db = SQLAlchemy(app)

#创建LoginManager对象，对会话进行管理
login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'

from . import models, views, forms