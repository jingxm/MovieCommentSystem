# coding: utf-8
import re
import requests
from bs4 import BeautifulSoup
from . import app, db
from werkzeug import security
from functools import wraps
from app.models import User, Movie, Comment
from app.forms import SearchForm, LoginForm, RegisterForm, MovieForm, SettingForm, CommentForm,ChangeCommentForm,ChangeMovieForm
from flask import render_template, redirect, url_for, flash, request, session
from flask_login import login_user, logout_user, login_required, current_user
from urllib2 import urlopen
from flask.ext.paginate import Pagination
import json
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import os

'''
电影评论系统视图层
url                     功能
/;/home                 主页，随机展示10个电影
/Login                  登录界面
/Logout                 登出用户
/Regist                 注册界面
/search                 搜索
/AddMovie               导入新电影
/PersonSetting             用户个人信息
'''
#404页面处理，返回主页
@app.errorhandler(404)
def page_not_found(error):
    flash('该页面不存在')
    return redirect(url_for('Home'))

# 对所有访客可见,管理员与用户都用此界面登录
@app.route('/Login',methods=['POST','GET'])
def Login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('Login.html', form=form)

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user is not None and user.password_verification(form.password.data):
                login_user(user)
                if current_user.id == 1:
                    flash('管理员登录成功！')
                else:
                    flash('登录成功！')
                return redirect(url_for('Home'))
            flash('用户名或密码错误！')
            return render_template('Login.html',form=form)
        else:
            flash('请检查是否输入用户名与密码')
            return render_template('Login.html',form=form)

# 对登录用户可见,重定向到登录界面
@app.route('/Logout', methods=['POST','GET'])
@login_required
def Logout():
    logout_user()
    flash('您已经成功登出！')
    return redirect(url_for('Home'))

# 对所有访客可见,主页显示8部电影
@app.route("/", methods=['POST', 'GET'])
@app.route('/Home', methods=['POST','GET'])
@app.route('/Home/<int:page>', methods=['POST', 'Get'])
def Home(page = 1):
    # = Movie.query.order_by('id').all()
    movie_list = Movie.query.order_by('id').paginate(page, 4, False)
    return render_template('MovieList.html', movie_list=movie_list)

# 对所有访客可见,用户注册，成功会跳转至主页面，否则回到本页面
@app.route('/Regist',methods=['POST','GET'])
def Regist():
    form = RegisterForm()
    if request.method == "GET":
        return render_template("Regist.html", form=form)

    if request.method == "POST":
        if form.validate_on_submit():
            if User.query.filter_by(username=form.username.data).first():
                flash('此用户名已被占用,请更换用户名注册')
                return redirect(url_for('Regist'))
            else:
                user = User(username=form.username.data,password=form.password2.data,
                            email=form.email.data,phone=form.phone.data)
                db.session.add(user)
                db.session.commit()
                flash('注册成功,跳转至主页')
                login_user(user)
                return redirect(url_for('Home'))
        else:
            flash("请检查是否输入全部内容、邮箱格式以及两个密码是否一致")
        return render_template('Regist.html',form=form)