import pytest
from ..app import OrderCalculator

@pytest.mark.parametrize(
    "quantity,price,expected",
    [
        (3, 5, 15),
        (1, 2, 2),
        (10, 7, 70),
    ],
)
def test_order_calcuator_get_price(quantity, price, expected):
    calculator = OrderCalculator(quantity, price)
    price = calculator.get_price()

    assert price == expected
