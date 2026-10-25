import allure
import pytest
from data import ORDER_DATA_BLACK, WITHOUT_TRACK, NOT_ENOUGH_DATA_FOR_SEARCH, INVALID_TRACK, ORDER_NOT_FOUND


class TestGetOrder:

    @allure.title('Успешное получение заказа')
    @allure.description('Тест проверяет код и тип id заказа при получении заказа')
    @pytest.mark.parametrize("order_data", [ORDER_DATA_BLACK])
    def test_get_order_status_code_201(self, order_by_track, order_data):
        status_code_get_order, id_order = order_by_track.get_order()
        assert status_code_get_order == 200 and isinstance(id_order, int), \
            f'Код ответа: {status_code_get_order}, возвращается: {type(id_order)}'

    @allure.title('Невозможно получение заказа без номера заказа в query-параметрах')
    @allure.description('Тест проверяет код ошибки и тело ответа при получении заказа без номера в query-параметрах')
    @pytest.mark.parametrize("order_data", [ORDER_DATA_BLACK])
    def test_get_order_without_track_status_code_400(self, order_by_track, order_data):
        status_code, response_body = order_by_track.get_order(WITHOUT_TRACK)
        assert status_code == 400 and NOT_ENOUGH_DATA_FOR_SEARCH in response_body, \
            f'Код ответа: {status_code}, тело ответа: {response_body}'

    @allure.title('Невозможно получение заказа c несуществующим номером заказа в в query-параметрах')
    @allure.description('Тест проверяет код ошибки и тело ответа при получении заказа без номера в query-параметрах')
    @pytest.mark.parametrize("order_data", [ORDER_DATA_BLACK])
    def test_get_order_invalid_track_status_code_404(self, order_by_track, order_data):
        status_code, response_body = order_by_track.get_order(INVALID_TRACK)
        assert status_code == 404 and ORDER_NOT_FOUND in response_body, \
            f'Код ответа: {status_code}, тело ответа: {response_body}'
