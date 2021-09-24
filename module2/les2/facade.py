class Ordering:

    def order(self):
        print('Ordering')


class Preparing:

    def prepare(self):
        print('Preparing')


class Delivering:

    def deliver(self):
        print('Delivering')


class Order:

    def __init__(self):
        self.ordering = Ordering()
        self.preparing = Preparing()
        self.delivering = Delivering()

    def complete_order(self):
        self.ordering.order()
        self.preparing.prepare()
        self.delivering.deliver()


if __name__ == '__main__':
    order = Order()
    order.complete_order()
