from methods.ored_methods import OrderMethods
import pytest_check as check
from data import *
from conftest import *

class TestCreateOrder:

    @allure.title('Система позволяет создать заказ авторизованному пользователю')
    def test_create_order(self, new_user_token):
        _, _, token = new_user_token
        order_data = BodyOrder.THREE_INGREDIENTS
        response = OrderMethods.create_order(order_data, token)
        check.equal(response.status_code, 200)
        check.is_in('name', response.json())
        check.is_in('order', response.json())
        check.is_in('number', response.json()['order'])
        check.equal(response.json()['success'], True)

    @allure.title('Система позволяет создать заказ неавторизованному пользователю')
    def test_create_order_no_token(self, new_user):
        _, _ = new_user
        order_data = BodyOrder.THREE_INGREDIENTS
        token = None
        response = OrderMethods.create_order(order_data, token)
        check.equal(response.status_code,200)
        check.is_in('name', response.json())
        check.is_in('order', response.json())
        check.is_in('number', response.json()['order'])
        check.equal(response.json()['success'], True)

    @allure.title('Система позоваляет создать заказ с ингредиентами')
    def test_create_order_with_ingredients(self, new_user_token):
        _, _, token = new_user_token
        order_data = BodyOrder.THREE_INGREDIENTS
        response = OrderMethods.create_order(order_data, token)
        check.equal(response.status_code, 200)
        check.is_in('name', response.json())
        check.is_in('order', response.json())
        check.is_in('number', response.json()['order'])
        check.equal(response.json()['success'], True)

    @allure.title('Система не разрешает создать заказ без инградиентов')
    def test_create_order_without_ingredients(self, new_user_token):
        _, _, token = new_user_token
        order_data = BodyOrder.ZERO_INGREDIENTS
        response = OrderMethods.create_order(order_data, token)
        check.equal(response.status_code, 400)
        check.equal(response.json(), BodyAnswer.ID_INGREDIENTS_REQUIRED)

    @allure.title('Система не позволяет создать заказ с неверным id инградиентов')
    def test_create_order_with_wrong_id_ingredients(self, new_user_token):
        _, _, token = new_user_token
        order_data = BodyOrder.WRONG_INGREDIENTS
        response = OrderMethods.create_order(order_data, token)
        check.equal(response.status_code, 500)
