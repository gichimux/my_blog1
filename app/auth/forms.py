from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from ..models import User



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),Email()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('rememberme', default=False)


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),Email()])
    nickname = StringField('Nickname', validators=[DataRequired(), Length(1, 64) ])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('This Email is already taken')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('The Username already exists')

#password changer form
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    password = PasswordField('New password', validators=[DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm new password', validators=[DataRequired()])