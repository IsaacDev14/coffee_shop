import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_initialization():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)
    
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
    assert order in Order._all_orders

def test_order_validation():
    customer = Customer("Bob")
    coffee = Coffee("Espresso")
    
    with pytest.raises(ValueError):
        Order("not a customer", coffee, 5.0)  # Invalid customer
    with pytest.raises(ValueError):
        Order(customer, "not a coffee", 5.0)  # Invalid coffee
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  # Price too low
    with pytest.raises(ValueError):
        Order(customer, coffee, 11.0)  # Price too high
    with pytest.raises(ValueError):
        Order(customer, coffee, "invalid")  # Invalid price type