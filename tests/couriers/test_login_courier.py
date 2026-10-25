import allure
import pytest
from data import REQUIRED_COURIER_DATA, INVALID_LOGIN, INVALID_PASSWORD, INVALID_LOGIN_OR_PASSWORD_MESSAGE, ONLY_LOGIN, \
    ONLY_PASSWORD, ONLY_LOGIN_OR_PASSWORD_MESSAGE, NOT_EXISTING_USER


class TestLoginCourier:

    @allure.title('Успешное получение id курьера')
    @allure.description('Тест проверяет код и тело ответа при получении id курьера')
    @pytest.mark.parametrize("courier_data", [REQUIRED_COURIER_DATA])
    def test_login_courier_status_code_200(self, courier, courier_data):
        status_code_login_courier, response_body_id_courier, _ = courier.get_id_courier(courier_data)
        assert status_code_login_courier == 200 and isinstance(response_body_id_courier, int), \
            f'Код ответа: {status_code_login_courier}, id: {response_body_id_courier}'


    @allure.title('Невозможно получить id курьера при неверном логине или/и пароле курьера')
    @allure.description('Тест проверяет код и тело ответа при неверном логине или/и пароле курьера')
    @pytest.mark.parametrize("courier_data, invalid_data", [[REQUIRED_COURIER_DATA, INVALID_LOGIN],
                                                            [REQUIRED_COURIER_DATA, INVALID_PASSWORD],
                                                            [REQUIRED_COURIER_DATA, NOT_EXISTING_USER],
                                                            ]
                             )
    def test_login_courier_invalid_login_or_password_status_code_404(self, courier, courier_data, invalid_data):
        status_code_login_courier, _, response_body_id_error = courier.get_id_courier(invalid_data)
        assert status_code_login_courier == 404 and INVALID_LOGIN_OR_PASSWORD_MESSAGE in response_body_id_error, \
            f'Код ответа: {status_code_login_courier}, id: {response_body_id_error}'


    @allure.title('Невозможно получить id курьера при пустом поле логина или пароля курьера')
    @allure.description('Тест проверяет код и тело ответа при пустом поле логина или пароля курьера')
    @pytest.mark.parametrize("courier_data, only_one_field", [[REQUIRED_COURIER_DATA, ONLY_LOGIN],
                                                            [REQUIRED_COURIER_DATA, ONLY_PASSWORD]
                                                            ]
                             )
    def test_login_courier_only_login_or_password_status_code_400(self, courier, courier_data, only_one_field):
        status_code_login_courier, _, response_body_id_error = courier.get_id_courier(only_one_field)
        assert status_code_login_courier == 400 and ONLY_LOGIN_OR_PASSWORD_MESSAGE in response_body_id_error, \
            f'Код ответа: {status_code_login_courier}, id: {response_body_id_error}'
