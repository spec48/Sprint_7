# Проект: Автотесты API сервиса «Яндекс.Самокат»
Протестированы ручки:
1. Создание курьера
2. Логин курьера
3. Создание заказа
4. Список заказов
5. Удалить курьера
6. Принять заказ
7. Получить заказ по его номеру
___
## Используемые библиотеки
- pytest
- allure
___
## Запустить автотесты можно командой ```pytest tests --alluredir=allure_results``` из папки проекта Sprint_7
## Запустить сервер allure командой ```allure serve ./allure_results```
___
## Структура проекта
- tests/ — python package с тестами.
  - couriers/  
    - test_create_courier.py - тесты создания курьера.
    - test_delete_courier.py - тесты удаления курьера.
    - test_login_courier.py - тесты логина курьера.
  - orders/
    - test_accept_order.py - тесты на принятие заказа.
    - test_create_order.py - тесты на создание заказа.
    - test_get_order.py - тесты на получение номера заказа.
    - test_get_orders_list.py - тесты на создание списка заказов.
- methods/ - python package с методами классов.
  - courier_methods.py - методы курьера.
  - order_methods.py - методы заказа.
- conftest.py — фикстуры.
- helpers.py — вспомогательные функции.
- urls.py — файл с url.
- data.py — файл с данными.
- README.md - описание проекта
- .gitignore
- requirements.txt
___