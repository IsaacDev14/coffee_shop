from order import Order

class Coffee:
    def __init__(self, name):
        self.name = name #use property setter for validation

        @property
        def name(self):
            return self._name
        
        @name.setter
        def name(Self, value):
            if not isinstance(value, str):
                raise ValueError("Name must be a string")
            if len(value) < 3:
                raise ValueError("Name must be at least 3 characters")
            self._name = name


        def orders(self):
            return [order for order in Order._all_orders if order.coffee == self]
        
        def customers(self):
            return list[set(order.customer for order in self.orders())]