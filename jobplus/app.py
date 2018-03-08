from flask import Flask, render_template
from jobplus.config import configs
from flask_migrate import Migrate
from jobplus.models import db, User
from flask_login import LoginManager

def register_blueprints(app):
	from .handlers import front
	app.register_blueprint(front)
def register_extension(app):
	#注册数据库
	db.init_app(app)
	Migrate(app, db)
	#登录功能扩展
	login_manager = LoginManager()
	login_manager.init_app(app)

	@login_manager.user_loader
	def user_loader(id):
		#登录扩展的回调函数，用来判断用户的登录状态
		return User.query.get(id)
	
	login_manager.login_view = 'front.login'


def create_app(config):
	""" App 工厂"""
	app = Flask(__name__)
	app.config.from_object(configs.get(config))

	register_blueprints(app)
	register_extension(app)
	# print(app.url_map)
	return app


