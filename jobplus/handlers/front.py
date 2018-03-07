from flask import Blueprint, render_template
from jobplus.models import db, Job
from jobplus.forms import *
# 省略了 url_prefix，那么默认就是 '/'
front = Blueprint('front', __name__)

@front.route('/')
def index():
	jobs = Job.query.all()
	return render_template('index.html', jobs=jobs)
@front.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	return render_template('login.html', form=form)
