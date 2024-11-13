from flask import Blueprint
from user_auth import register

befa = Blueprint('befa', __name__)


@befa.post('/register')
def register_route():
    return register()
