import os
from .local import *

basedir = os.path.abspath(os.path.dirname(__file__) + '/../../..')

DEVELOPMENT = True
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_DATABASE_URI = '{DRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}'.format(**DB_CONFIG)