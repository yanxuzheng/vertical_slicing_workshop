import argparse
class OrderCalculator:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price


    def get_price(self):
        """Get price for Order."""
        return round(self.price * self.quantity * (1 + self.get_tax_rate()), 2)

    def get_tax_rate(self):
        # tax rate for CA
        return 0.0825


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--quantity', type=int)
    parser.add_argument('-p', '--price', type=int)
    args = parser.parse_args()
    calculator = OrderCalculator(quantity=args.quantity, price=args.price)
    order_value = calculator.get_price()
    print(order_value)


if __name__ == "__main__":
    main()
