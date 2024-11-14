from flask import Blueprint
from user_auth import register, login
from news_api import get_news

befa = Blueprint('befa', __name__)


@befa.post('/register')
def register_route():
    return register()


@befa.post('/login')
def login_route():
    return login()


@befa.get('/news')
def news_api_route():
    return get_news()

