import random
import json


from flask import render_template


from app import db
from .forms import UserCreateForm
from .models import User
from . import users


@users.route('/')
def index():
    users = User.query.filter_by().all()
    return render_template('users.html', context=users)

@users.route('/list')
def get_users_list():
    users = User.query.filter_by().all()
    data = {}
    for user in users:
        data[user.id] = user.username
    return json.dumps({'status': '200', 'users': data})


@users.route('/delete/<int:id>/')
def delete_user(*args, **kwargs):

    if User.query.filter_by(id=kwargs['id']).first():

        user = User.query.filter_by(id=kwargs['id']).first()
        db.session.delete(user)
        db.session.commit()

        return json.dumps({'status': '200'})
    else:
        return json.dumps({'status': '400'})



@users.route('/create', methods=['GET', 'POST'])
def create_user():

    form = UserCreateForm()

    if User.query.filter_by(username=form.username.data).first() is not None:
        return json.dumps({'status': '400', "message": 'Wrong name'})

    elif form.username.data is "":
        return json.dumps({'status': '422', "message": 'No value'})

    else:
        user = User(username=form.username.data)
        db.session.add(user)
        db.session.commit()

        return json.dumps({'status': '200'})


@users.route('/winners')
def get_random_users():
    users = User.query.filter_by().all()
    users = random.sample(set(users), 3)
    winners = []
    for user in users:
        winners.append(user.username)
    return json.dumps({'status': '200', 'users': winners})

