from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from jobplus.models import db, Job, User
from jobplus.forms import *
from flask_login import login_user, logout_user, login_required

# 省略了 url_prefix，那么默认就是 '/'
# 加上了url_prefix='/', 那么login的路由就变成 host//login了！！！ 两个'/'
front = Blueprint('front', __name__)

@front.route('/')
@front.route('/index')
def index():
	# print(session)
	jobs = Job.query.all()
	return render_template('index.html', jobs=jobs)
@front.route('/login', methods=['GET', 'POST'])
def login():
	#判断用户的登录状态
	if session.get('user_id'):
		flash('您已登录', 'info')
		return redirect(url_for('front.index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user:
			login_user(user, form.remember_me.data)
			return redirect(url_for('front.index'))
		else:
			flash('账号与密码不匹配', 'danger')
	return render_template('login.html', form=form)

@front.route('/logout')
@login_required
def logout():
	logout_user()
	flash("注销成功", "success")
	# print("logout")
	return redirect(url_for('front.index'))