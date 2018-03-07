from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Length, Email, EqualTo, Required

class LoginForm(FlaskForm):
    email = StringField('邮箱账号', validators=[Required(), Email(), Length(3,30)])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')