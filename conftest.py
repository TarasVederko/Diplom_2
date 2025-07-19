import allure
import pytest
from generator import generator_user_body
from methods.user_methods import UserMethods

@pytest.fixture
def new_user():
    body = generator_user_body()
    response = UserMethods.create_new_user(body)
    yield response, body

@pytest.fixture
def new_user_token(new_user):
    _, body = new_user
    response = UserMethods.login_user(body)
    token = response.json()['accessToken']
    yield response, body, token
