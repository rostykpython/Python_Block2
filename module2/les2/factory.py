class Pizza:
    def __init__(self, price: float):
        self.price = price

    def get_price(self) -> float:
        return self.price


class PizzaMargarita(Pizza):
    def __init__(self, price):
        super(PizzaMargarita, self).__init__(price)


class PizzaMexico(Pizza):
    def __init__(self):
        super(PizzaMexico, self).__init__(5.5)


class PizzaCarbonara(Pizza):
    def __init__(self):
        super(PizzaCarbonara, self).__init__(9.5)


def create_pizza(pizza_type: Pizza) -> None:
    print('Creating pizza!')
    ready_pizza = pizza_type.get_price()
    print(f'Please pay {ready_pizza}$')


if __name__ == '__main__':
    create_pizza(PizzaCarbonara())