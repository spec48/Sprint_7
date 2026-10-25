import allure
import requests
from urls import BASE_URL, ORDER_URL


class OrderMethods:

    def __init__(self):
        self.url = f'{BASE_URL}{ORDER_URL}'
        self._track = None
        self.id_order = None

    @allure.step("Создать заказ")
    def create_order(self, params=None):
        response = requests.post(self.url, json=params)
        self._track = response.json().get("track")
        return response.status_code, response.json().get("track")

    @allure.step('Получить заказ')
    def get_order(self, params=None):
        if params is None:
            track = self._track
        else:
            track = params
        response = requests.get(f'{self.url}/track?t={track}')
        try:
            self.id_order = response.json().get("order").get("id")
            return response.status_code, response.json().get("order").get("id")
        except AttributeError:
            return response.status_code, response.text

    @allure.step('Получить список заказов')
    def get_orders_list(self, id_courier):
        response = requests.get(f'{self.url}?courierId={id_courier}')
        return response.status_code, response.json().get("orders"), len(response.json().get("orders"))

    @allure.step('Принять заказ')
    def accept_order(self, id_order, id_courier):
        if id_order is None:
            id_order = self.id_order
        response = requests.put(f'{self.url}/accept/{id_order}?courierId={id_courier}')
        return response.status_code, response.text

    @allure.step('Завершить заказ')
    def finish_order(self):
        response = requests.put(f'{self.url}/finish/{self.id_order}')
        return response.status_code
