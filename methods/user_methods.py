import allure
import requests
from url import EndPoints


class UserMethods:

    @staticmethod
    @allure.step('Создаем нового пользователя')
    def create_new_user(body):
        return requests.post(EndPoints.CREATE_USER, json=body)

    @staticmethod
    @allure.step('Логинимся')
    def login_user(body):
        email = body['email']
        password = body['password']
        return requests.post(EndPoints.LOGIN_USER, json = {'email': email, 'password': password})
