from flask import Blueprint

api = Blueprint('api', __name__)

from . import auth, posts, users, comments, errors