from flask import Blueprint
from user_auth import register, login

befa = Blueprint('befa', __name__)


@befa.post('/register')
def register_route():
    return register()


@befa.post('/login')
def login_route():
    return login()
