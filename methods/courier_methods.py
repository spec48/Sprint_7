import allure
import requests
from urls import BASE_URL, COURIER_URL


class CourierMethods:

    def __init__(self, params):
        self.url = f'{BASE_URL}{COURIER_URL}'
        self.params = params
        self.id_courier = None
        self._created = False

    @allure.step("Создать курьера")
    def create_courier(self):
        response = requests.post(self.url, data=self.params)
        if response.status_code == 201:
            self._created = True
        return response.status_code, response.text

    @allure.step("Получить id курьера")
    def get_id_courier(self, params=None):
        if params is None:
            params = self.params
        if not self._created:
            return 404, {"message": "Курьер не создан."}
        response = requests.post(f'{self.url}login', data=params)
        self.id_courier = response.json().get("id")
        return response.status_code, response.json().get("id"), response.json().get("message")

    @allure.step("Удалить курьера")
    def delete_courier(self, params=None):
        if params is None:
            id_courier = self.id_courier
        else:
            id_courier = params
        if self.id_courier is None:
            return 404, {"message": "Курьера с таким id нет."}
        response = requests.delete(f'{self.url}{id_courier}')
        return response.status_code, response.text
