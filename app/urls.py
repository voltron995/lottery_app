from . import app
from .users import users

app.register_blueprint(users, url_prefix='/users')
