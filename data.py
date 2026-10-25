from helpers import generate_courier_data


CREATE_COURIER_SUCCESS = '{"ok":true}'
DELETE_COURIER_SUCCESS = '{"ok":true}'
ACCEPT_ORDER_SUCCESS = '{"ok":true}'

CREATE_ERROR_RESPONSE_BODY_TEXT = 'Этот логин уже используется'
NOT_ENOUGH_DATA_TO_CREATE = 'Недостаточно данных для создания учетной записи'
NOT_ENOUGH_DATA_TO_DELETE = 'Недостаточно данных для удаления курьера'
NOT_ENOUGH_DATA_FOR_SEARCH = 'Недостаточно данных для поиска'
ORDER_NOT_FOUND = 'Заказ не найден'
INVALID_LOGIN_OR_PASSWORD_MESSAGE = 'Учетная запись не найдена'
INVALID_ID_MESSAGE = 'Курьера с таким id нет'
INVALID_COURIER = 'Курьера с таким id не существует'
ONLY_LOGIN_OR_PASSWORD_MESSAGE = 'Недостаточно данных для входа'

ALL_COURIER_DATA = generate_courier_data()[0]
LOGIN_IN_COURIER_DATA = generate_courier_data()[1]
PASSWORD_COURIER_DATA = generate_courier_data()[2]
REQUIRED_COURIER_DATA = {
            "login": "UniqueCourier123",
            "password": "123456"
}
INVALID_LOGIN = {
            "login": "UniqueCourier456",
            "password": "123456"
}
INVALID_PASSWORD = {
            "login": "UniqueCourier123",
            "password": "654321"
}
NOT_EXISTING_USER = {
            "login": "UnknownUser",
            "password": "098765"
}
ONLY_LOGIN = {
            "login": "UniqueCourier123",
            "password": ""
}
ONLY_PASSWORD = {
            "login": "",
            "password": "123456"
}
BASE_ORDER_DATA = {
    "firstName": "Николай",
    "lastName": "Петров",
    "address": "Техноград, д.25, кв.1",
    "metroStation": 1,
    "phone": "8003553535",
    "rentTime": 3,
    "deliveryDate": "2026-10-30",
    "comment": " Комментарий: домофон"
}
ORDER_DATA_BLACK = {**BASE_ORDER_DATA, "color": ["BLACK"]}
ORDER_DATA_GREY = {**BASE_ORDER_DATA, "color": ["GREY"]}
ORDER_DATA_BOTH = {**BASE_ORDER_DATA, "color": ["BLACK", "GREY"]}
ORDER_DATA_EMPTY = {**BASE_ORDER_DATA, "color": []}

LENGTH_ORDERS_LIST = 1
WITHOUT_ID_COURIER = ""
INVALID_ID_COURIER = "88888888"

WITHOUT_TRACK = ""
INVALID_TRACK = "88888888"

WITHOUT_ID_ORDER = ""
INVALID_ID_ORDER = "88888888"
