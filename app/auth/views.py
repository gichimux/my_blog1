from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from .. import db
from .forms import LoginForm, RegisterForm, ChangePasswordForm
from ..models import User
from . import auth
from ..main.forms import SearchForm


@auth.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now()
        db.session.add(current_user)
        db.session.commit()
    g.search_form = SearchForm()

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('The email or password is invalid')
    return render_template('auth/login.html',title = 'log in',form =form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('user has been logged out')
    return redirect(url_for('user.index'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    nickname=form.nickname.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Log In to proceed')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form=form,title='registered')

@auth.route('/changepassword', methods=['GET','POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            db.session.add(current_user)
            db.session.commit()
            flash('Your password has been Changed')
            return redirect(url_for('user.index'))
        else:
            flash('Password not Changed')
    return render_template('auth/change_password.html',form=form,title='Change The Password')