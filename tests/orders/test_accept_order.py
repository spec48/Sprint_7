import allure
import pytest
from data import (ORDER_DATA_BLACK, NOT_ENOUGH_DATA_FOR_SEARCH, ALL_COURIER_DATA, ACCEPT_ORDER_SUCCESS, INVALID_COURIER,
                  WITHOUT_ID_ORDER, INVALID_ID_ORDER, WITHOUT_ID_COURIER, INVALID_ID_COURIER)


class TestAcceptOrder:

    @allure.title('Успешное принятие заказа')
    @allure.description('Тест проверяет код и тело ответа при приеме заказа')
    @pytest.mark.parametrize("courier_data, order_data", [[ALL_COURIER_DATA, ORDER_DATA_BLACK]])
    def test_accept_order_valid_id_order_and_valid_id_courier_status_code_200(self, order_to_accept, courier_data, order_data):
        status_code_accept_order, response_body = order_to_accept[0].accept_order(id_order=order_to_accept[1],
                                                                                  id_courier=order_to_accept[2])
        assert status_code_accept_order == 200 and response_body == ACCEPT_ORDER_SUCCESS, \
            f'Код ответа: {status_code_accept_order}, тело ответа: {response_body}'


    @allure.title('Невозможно принять заказ при отсутствии id заказа и существующим id курьера')
    @allure.description('Тест проверяет код и тело ответа при приеме заказа с существующем id заказа и '
                        'существующим id курьера')
    @pytest.mark.parametrize("courier_data, order_data", [[ALL_COURIER_DATA, ORDER_DATA_BLACK]])
    def test_accept_order_without_id_order_and_valid_id_courier_status_code_400(self, order_to_accept, courier_data, order_data):
        status_code_accept_order, response_body = order_to_accept[0].accept_order(id_order=WITHOUT_ID_ORDER,
                                                                                  id_courier=order_to_accept[2])
        assert status_code_accept_order == 400 and NOT_ENOUGH_DATA_FOR_SEARCH in response_body, \
            f'Код ответа: {status_code_accept_order}, тело ответа: {response_body}'


    @allure.title('Невозможно принять заказ при несуществующем id заказа и существующим id курьера')
    @allure.description('Тест проверяет код и тело ответа при приеме заказа с несуществующим id заказа и '
                        'существующим id курьера')
    @pytest.mark.parametrize("courier_data, order_data", [[ALL_COURIER_DATA, ORDER_DATA_BLACK]])
    def test_accept_order_invalid_id_order_and_valid_id_courier_status_code_404(self, order_to_accept, courier_data, order_data):
        status_code_accept_order, response_body = order_to_accept[0].accept_order(id_order=INVALID_ID_ORDER,
                                                                                  id_courier=order_to_accept[2])
        assert status_code_accept_order == 404 and 'Заказа с таким id не существует' in response_body, \
            f'Код ответа: {status_code_accept_order}, тело ответа: {response_body}'


    @allure.title('Невозможно принять заказ при существующем id заказа и отсутствии id курьера')
    @allure.description('Тест проверяет код и тело ответа при приеме заказа с существующим id заказа и без id курьера')
    @pytest.mark.parametrize("courier_data, order_data", [[ALL_COURIER_DATA, ORDER_DATA_BLACK]])
    def test_accept_order_valid_id_order_and_without_id_courier_status_code_400(self, order_to_accept, courier_data, order_data):
        status_code_accept_order, response_body = order_to_accept[0].accept_order(id_order=order_to_accept[1],
                                                                                  id_courier=WITHOUT_ID_COURIER)
        assert status_code_accept_order == 400 and NOT_ENOUGH_DATA_FOR_SEARCH in response_body, \
            f'Код ответа: {status_code_accept_order}, тело ответа: {response_body}'


    @allure.title('Невозможно принять заказ при существующем id заказа и несуществующем id курьера')
    @allure.description('Тест проверяет код и тело ответа при приеме заказа с существующим id заказа и '
                        'несуществующем id курьера')
    @pytest.mark.parametrize("courier_data, order_data", [[ALL_COURIER_DATA, ORDER_DATA_BLACK]])
    def test_accept_order_valid_id_order_and_invalid_id_courier_status_code_404(self, order_to_accept, courier_data, order_data):
        status_code_accept_order, response_body = order_to_accept[0].accept_order(id_order=order_to_accept[1],
                                                                                  id_courier=INVALID_ID_COURIER)
        assert status_code_accept_order == 404 and INVALID_COURIER in response_body, \
            f'Код ответа: {status_code_accept_order}, тело ответа: {response_body}'
