import pytest
from ..app import OrderCalculator

@pytest.mark.parametrize(
    "quantity,price,state,expected",
    [
        (3, 5, "CA", 16.24),
        (3, 5, "TX", 15.94),
        (1, 2, "CA", 2.17),
        (10, 7, "CA", 75.78),
    ],
)
def test_order_calcuator_get_price(quantity, price, state, expected):
    calculator = OrderCalculator(quantity=quantity, price=price, state=state)
    price = calculator.get_price()

    assert price == expected
