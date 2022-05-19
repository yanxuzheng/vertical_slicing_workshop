from app import OrderCalculator

def test_order_calcuator_get_price():
    price = OrderCalculator().get_price()

    assert price == "hello_world"
