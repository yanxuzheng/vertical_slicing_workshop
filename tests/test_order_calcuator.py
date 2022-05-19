import pytest
from ..app import OrderCalculator

@pytest.mark.parametrize(
    "quantity,price,expected",
    [
        (3, 5, 16.24),
        (1, 2, 2.17),
        (10, 7, 75.78),
    ],
)
def test_order_calcuator_get_price(quantity, price, expected):
    calculator = OrderCalculator(quantity=quantity, price=price)
    price = calculator.get_price()

    assert price == expected
