from flask import Flask, render_template
from jobplus.config import configs
from flask_migrate import Migrate
from jobplus.models import db

def register_blueprints(app):
	from .handlers import front
	app.register_blueprint(front)

def create_app(config):
	""" App 工厂"""
	app = Flask(__name__)
	app.config.from_object(configs.get(config))
	db.init_app(app)
	Migrate(app, db)
	register_blueprints(app)
	return app
