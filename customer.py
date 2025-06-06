class Customer:
    def __init__(self, name):
        self.name = name  # Use property setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        from order import Order  # local import to break circular import
        return [order for order in Order._all_orders if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        from order import Order  # local import
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from coffee import Coffee
        if not isinstance(coffee, Coffee):
            raise ValueError("Coffee must be a Coffee instance")
        spent_by_customer = {}
        for order in coffee.orders():
            spent_by_customer[order.customer] = (
                spent_by_customer.get(order.customer, 0) + order.price
            )
        if not spent_by_customer:
            return None
        return max(spent_by_customer, key=spent_by_customer.get)
