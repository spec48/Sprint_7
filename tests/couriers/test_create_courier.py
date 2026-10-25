import allure
import pytest
from data import CREATE_COURIER_SUCCESS, REQUIRED_COURIER_DATA, ALL_COURIER_DATA, \
    CREATE_ERROR_RESPONSE_BODY_TEXT, NOT_ENOUGH_DATA_TO_CREATE, LOGIN_IN_COURIER_DATA, PASSWORD_COURIER_DATA


class TestCreateCourier:

    @allure.title('Успешное создание курьера с обязательными полями')
    @allure.description('Тест проверяет код и тело ответа при создании курьера с обязательными полями')
    @pytest.mark.parametrize("courier_data", [ALL_COURIER_DATA, REQUIRED_COURIER_DATA])
    def test_create_courier_with_login_and_password_status_code_201(self, courier_configure, courier_data):
        status_code, response_body = courier_configure.create_courier()
        assert status_code == 201 and response_body == CREATE_COURIER_SUCCESS, \
            f'Код ответа: {status_code}, тело ответа: {response_body}'

    @allure.title('Невозможно создание двух одинаковых курьеров с одинаковым логином')
    @allure.description('Тест проверяет код ошибки и тело ответа при создании курьера с логином, который уже есть')
    @pytest.mark.parametrize("courier_data", [ALL_COURIER_DATA])
    def test_create_courier_two_identical_couriers_status_code_409(self, courier, courier_data):
        status_code_create_error, response_body_create_error = courier.create_courier()
        assert status_code_create_error == 409 and CREATE_ERROR_RESPONSE_BODY_TEXT in response_body_create_error, \
            f'Код ответа: {status_code_create_error}, тело ответа: {response_body_create_error}'

    @allure.title('Невозможно создание курьера с одним обязательным полем')
    @allure.description('Тест проверяет код ошибки и тело ответа при создании курьера с одним обязательным полем')
    @pytest.mark.parametrize("courier_data", [LOGIN_IN_COURIER_DATA, PASSWORD_COURIER_DATA])
    def test_create_courier_with_login_or_password_status_code_400(self, courier_configure, courier_data):
        status_code_create_error, response_body_create_error = courier_configure.create_courier()
        assert status_code_create_error == 400 and NOT_ENOUGH_DATA_TO_CREATE in response_body_create_error, \
            f'Код ответа: {status_code_create_error}, тело ответа: {response_body_create_error}'
