from conftest import *
import pytest_check as check
from data import BodyAnswer

class TestLoginUser:

   @allure.title('Зарегистрированный пользователь может залогинится')
   def test_login_existed_user(self, new_user):
       response, body = new_user
       response = UserMethods.login_user(body)
       check.equal(response.status_code, 200)
       check.equal(response.json()['success'], True)

   @pytest.mark.parametrize('wrong_data', ['email', 'password'])
   @allure.title('Система сообщает об ошибке при вводе неверного логина или пароля')
   def test_login_wrong_data(self, new_user, wrong_data):
       _, body = new_user
       body_wrong = body
       body_wrong[wrong_data] = body[wrong_data][::-1]
       response = UserMethods.login_user(body_wrong)
       check.equal(response.status_code, 401)
       check.equal(response.json(), BodyAnswer.WRONG_EMAIL_OR_PASSWORD)
