import allure
import pytest
from data import ORDER_DATA_BLACK, ORDER_DATA_GREY, ORDER_DATA_BOTH, ORDER_DATA_EMPTY, REQUIRED_COURIER_DATA


class TestCreateOrder:

    @allure.title('Успешное создание заказа')
    @allure.description('Тест проверяет код ответа и тип при создании заказа с различными комбинациями поля "color"')
    @pytest.mark.parametrize("courier_data, order_data", [
        [REQUIRED_COURIER_DATA, ORDER_DATA_BLACK],
        [REQUIRED_COURIER_DATA, ORDER_DATA_GREY],
        [REQUIRED_COURIER_DATA, ORDER_DATA_BOTH],
        [REQUIRED_COURIER_DATA, ORDER_DATA_EMPTY]
    ]
                             )
    def test_create_order_status_code_201(self, order_configure, courier_data, order_data):
        status_code_create_order, response_body_create_order = order_configure.create_order(order_data)
        assert status_code_create_order == 201 and isinstance(response_body_create_order, int), \
            f'Код ответа: {status_code_create_order}'
