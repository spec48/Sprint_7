import allure
import pytest
from data import ALL_COURIER_DATA, LENGTH_ORDERS_LIST, ORDER_DATA_BLACK


class TestGetOrdersList:

    @allure.title('Успешное получение списка заказов')
    @allure.description('Тест проверяет код ответа, тип и длину списка при получении списка заказов')
    @pytest.mark.parametrize("courier_data, order_data", [[ALL_COURIER_DATA, ORDER_DATA_BLACK]])
    def test_get_orders_list_status_code_200(self, orders_list, courier_data, order_data):
        status_code, list_of_orders, length_list_of_orders = orders_list[0].get_orders_list(orders_list[1])
        assert status_code == 200 and isinstance(list_of_orders, list) and length_list_of_orders == LENGTH_ORDERS_LIST, \
            f'Код ответа: {status_code}, возвращается: {type(list_of_orders)}, длина списка: {length_list_of_orders}'
