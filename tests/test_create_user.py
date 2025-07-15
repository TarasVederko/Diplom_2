import allure
import pytest
from conftest import *
from data import BodyAnswer
import pytest_check as check


class TestCreateNewUser:

    @allure.title('Проверяем возможность зарегистировать нового пользователя')
    def test_successful_create_new_user(self, new_user):
        response,_ = new_user
        check.equal(response.status_code, 200)
        check.equal(response.json()['success'], True)


    @allure.title('Система не позволяет зарегистриовать пользователя с такими же данными')
    def test_error_create_same_user(self, new_user):
        _, body = new_user
        response = UserMethods.create_new_user(body)
        check.equal(response.status_code, 403)
        check.equal(response.json(), BodyAnswer.USER_ALREADY_EXIST)


    @pytest.mark.parametrize('missing_field', ['email', 'password', 'name'])
    @allure.title('Система сообщает об ошибке при регистрации, если не заполнено хотя бы одно обязательное поле')
    def test_error_create_user_missed_data(self, missing_field):
        body = generator_user_body()
        body[missing_field] = ''
        response = UserMethods.create_new_user(body)
        check.equal(response.status_code, 403)
        check.equal(response.json(), BodyAnswer.ALL_FIELDS_ARE_REQUIRED)
