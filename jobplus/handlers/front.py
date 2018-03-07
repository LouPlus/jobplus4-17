from flask import Blueprint, render_template
from jobplus.models import db, Job

# 省略了 url_prefix，那么默认就是 '/'
front = Blueprint('front', __name__, url_prefix='/', static_folder='static')

@front.route('/')
def index():
	jobs = Job.query.all()
	return render_template('index.html', jobs=jobs)
@front.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('login.html')
