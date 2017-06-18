import random
import json

from flask import redirect, render_template, flash, url_for

from app import db
from .forms import UserCreateForm
from .models import User
from . import users


@users.route('/')
def get_users_list():
    users = User.query.filter_by().all()
    return render_template('users.html', context=users)

@users.route('/delete/<int:id>/')
def delete_user(*args, **kwargs):
    user = User.query.filter_by(id=kwargs['id']).first()
    db.session.delete(user)
    db.session.commit()

    flash('You have successfully removed user.')
    return redirect(url_for('users.get_users_list'))

@users.route('/create', methods=['GET', 'POST'])
def create_user():

    form = UserCreateForm()
    if form.validate_on_submit():

        if User.query.filter_by(username=form.username.data).first():
            flash('This username is currently registered')
            print('first')
        else:
            user = User(username=form.username.data)
            db.session.add(user)
            db.session.commit()
            flash('User successfully created')
            print('second')

        return redirect(url_for('users.get_users_list'))

    return render_template('form.html', form=form, title='Add')


@users.route('/winners')
def get_random_users():
    users = User.query.filter_by().all()
    users = random.sample(set(users), 3)
    winners = []
    for user in users:
        winners.append(user.username)
    return json.dumps({'status': 'OK', 'users': winners})

