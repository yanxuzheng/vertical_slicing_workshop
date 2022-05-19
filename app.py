import argparse
class OrderCalculator:
    def __init__(self, quantity, price, state):
        self.quantity = quantity
        self.price = price
        self.state = state
        self.tax_rates = {
            "CA": 0.0825,
            "TX": 0.0625,
            "UT": 0.0685,
            "NV": 0.08,
            "AL": 0.04,
        }


    def get_price(self):
        """Get price for Order."""
        return round(self.price * self.quantity * (1 + self.get_tax_rate()), 2)

    def get_tax_rate(self):
        return self.tax_rates[self.state]



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--quantity', type=int)
    parser.add_argument('-p', '--price', type=int)
    parser.add_argument('-s', '--state', type=str)
    args = parser.parse_args()
    calculator = OrderCalculator(quantity=args.quantity, price=args.price, state=args.state)
    order_value = calculator.get_price()
    print(order_value)


if __name__ == "__main__":
    main()
