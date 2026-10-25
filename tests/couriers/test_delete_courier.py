import allure
import pytest
from data import ALL_COURIER_DATA, DELETE_COURIER_SUCCESS, NOT_ENOUGH_DATA_TO_DELETE, INVALID_ID_MESSAGE, \
    WITHOUT_ID_COURIER, INVALID_ID_COURIER


class TestDeleteCourier:

    @allure.title('Успешное удаление курьера')
    @allure.description('Тест проверяет код и тело ответа при удалении курьера с существующим id')
    @pytest.mark.parametrize("courier_data", [ALL_COURIER_DATA])
    def test_delete_courier_status_code_200(self, courier_to_del, courier_data):
        status_code, response_boby = courier_to_del.delete_courier()
        assert status_code == 200 and response_boby == DELETE_COURIER_SUCCESS, \
            f'Код ответа: {status_code}, тело ответа: {response_boby}'

    @allure.title('Невозможно удаление курьера без id в url')
    @allure.description('Тест проверяет код ошибки и тело ответа при удалении курьера без id')
    @pytest.mark.parametrize("courier_data", [ALL_COURIER_DATA])
    def test_delete_courier_without_id_status_code_400(self, courier_to_del, courier_data):
        status_code, response_boby = courier_to_del.delete_courier(WITHOUT_ID_COURIER)
        assert status_code == 400 and NOT_ENOUGH_DATA_TO_DELETE in response_boby, \
            f'Код ответа: {status_code}, тело ответа: {response_boby}'

    @allure.title('Невозможно удаление курьера с несуществующим id в url')
    @allure.description('Тест проверяет код ошибки и тело ответа при удалении курьера с несуществующим id в url')
    @pytest.mark.parametrize("courier_data", [ALL_COURIER_DATA])
    def test_delete_courier_invalid_id_status_code_404(self, courier_to_del, courier_data):
        status_code, response_boby = courier_to_del.delete_courier(INVALID_ID_COURIER)
        assert status_code == 404 and INVALID_ID_MESSAGE in response_boby, \
            f'Код ответа: {status_code}, тело ответа: {response_boby}'
