import allure
import requests
from url import EndPoints

class OrderMethods:

    @staticmethod
    @allure.step('Создаем заказа')
    def create_order(order_data, token):
        headers = {"Authorization": token}
        response =  requests.post(EndPoints.CREATE_ORDER, headers=headers, json=order_data)
        return response
