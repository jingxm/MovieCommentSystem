#-*-coding:utf-8-*-
import sys
from app import app, db
from app.models import Movie, User
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

"""编码设置"""
reload(sys)
sys.setdefaultencoding('utf-8')

manager = Manager(app)
migrate = Migrate(app, db)
admin = Admin(app, name='MovieSystem')

def make_shell_context():
    """自动加载环境"""
    return dict(
        app=app,
        db=db,
        Movie=Movie,
        User=User
    )

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(host = "0.0.0.0", port=8080))
admin.add_view(ModelView(Movie, db.session))
admin.add_view(ModelView(User, db.session))

@manager.command
def test():
    """运行测试"""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    app.debug = True
    manager.run()