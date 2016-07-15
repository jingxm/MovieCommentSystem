# 电影评论系统
---
* ##项目说明
 
    ###本项目是模仿豆瓣设计的一个电影信息查看、评论系统，使用了Python语言配合Flask框架，数据库使用SQLite。

# 部署方法
---
* ### 1.将源码放置在一个纯英文路径中，打开app文件夹下的__init__.py文件设置数据库路径。例如项目在C盘根目录替换为"sqlite:///C:/CODE/data.sqlite"
* ### 2.安装python2.7，PIP，在根目录下打开命令行执行pip install -r requirements.txt安装依赖
* ### 3.在根目录下打开命令行，键入python manage.py runserver启动后台服务器
* ### 4.通过访问127.0.0.1:8080来访问此项目网站(有需要可以在manage.py中修改IP和端口)
