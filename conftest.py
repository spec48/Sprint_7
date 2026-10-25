import pytest
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture()
def courier_configure(courier_data):
    courier_methods = CourierMethods(courier_data)
    yield courier_methods
    courier_methods.get_id_courier()
    courier_methods.delete_courier()

@pytest.fixture()
def courier(courier_configure):
    courier_configure.create_courier()
    return courier_configure

@pytest.fixture()
def order_configure():
    order_methods = OrderMethods()
    return order_methods

@pytest.fixture()
def courier_to_del(courier):
    courier.get_id_courier()
    return courier

@pytest.fixture()
def order_by_track(order_configure, order_data):
    order_configure.create_order(order_data)
    return order_configure

@pytest.fixture()
def order_to_accept(courier, order_configure, order_data):
    order_configure.create_order(order_data)
    order_configure.get_order()
    courier.get_id_courier()
    return order_configure, order_configure.id_order, courier.id_courier

@pytest.fixture()
def orders_list(order_to_accept):
    order_to_accept[0].accept_order(id_order=order_to_accept[1],
                                    id_courier=order_to_accept[2])
    return order_to_accept[0], order_to_accept[2]
