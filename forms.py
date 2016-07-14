# coding: utf-8

from flask_wtf import Form
from wtforms import IntegerField, StringField, SubmitField, PasswordField, BooleanField, DateField, FloatField
from wtforms.validators import Required, EqualTo, Email

'''注册表单'''
class RegisterForm(Form):
    username = StringField('用户名', validators=[Required()])
    password1 = PasswordField('密码', validators=[Required(), EqualTo('password2', message="密码匹配")])
    password2 = PasswordField('确认密码', validators=[Required()])
    email = StringField('邮箱', validators=[Required(), Email()])
    phone = StringField('电话', validators=[Required()])
    submit = SubmitField('注册')

'''登录表单'''
class LoginForm(Form):
    username = StringField('username', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('remember_me')
    submit = SubmitField('登录')

'''搜索表单'''
class SearchForm(Form):
    name = StringField('完整电影名称', validators=[Required()])
    submit = SubmitField('搜索')

'''新增电影信息'''
class MovieForm(Form):
    name = StringField('电影名称', validators=[Required()])
    submit = SubmitField('新增')

'''管理个人信息'''
class SettingForm(Form):
    old_password = PasswordField('原密码', validators=[Required()])
    password1 = PasswordField('密码', validators=[EqualTo('password2', message="密码匹配")])
    password2 = PasswordField('确认密码')
    email = StringField('邮箱', validators=[Email()])
    phone = StringField('电话')
    submit = SubmitField('保存')

'''发表评论表单'''
class CommentForm(Form):
    title = StringField('标题', validators=[Required()])
    content = StringField('评论', validators=[Required()])
    rating = FloatField('评分', validators=[Required()])
    submit = SubmitField('发表')

'''修改评论信息表单'''
class ChangeCommentForm(Form):
    rating = FloatField('评分', validators=[Required()])
    content = StringField('评论', validators=[Required()])
    submit = SubmitField('保存')

'''修改电影信息表单'''
class ChangeMovieForm(Form):
    name = StringField('电影名称', validators=[Required()])
    director = StringField('导演', validators=[Required()])
    summary = StringField('简介', validators=[Required()])
    actor = StringField('演员', validators=[Required()])
    date = DateField('上映日期', validators=[Required()])
    submit = SubmitField('保存')