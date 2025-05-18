import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    customer = Customer("Alice")
    assert customer.name == "Alice"
    
    with pytest.raises(ValueError):
        Customer("")  # Too short
    with pytest.raises(ValueError):
        Customer("A" * 16)  # Too long
    with pytest.raises(ValueError):
        Customer(123)  # Not a string

def test_customer_orders_and_coffees():
    customer = Customer("Bob")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)
    
    assert len(customer.orders()) == 1
    assert customer.orders()[0] == order
    assert len(customer.coffees()) == 1
    assert customer.coffees()[0] == coffee

def test_create_order():
    customer = Customer("Alice")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 3.5)
    
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 3.5
    with pytest.raises(ValueError):
        customer.create_order("not a coffee", 5.0)  # Invalid coffee

def test_most_aficionado():
    coffee = Coffee("Mocha")
    alice = Customer("Alice")
    bob = Customer("Bob")
    
    alice.create_order(coffee, 5.0)
    alice.create_order(coffee, 3.0)
    bob.create_order(coffee, 4.0)
    
    aficionado = Customer.most_aficionado(coffee)
    assert aficionado == alice  # Alice spent $8, Bob spent $4
    
    empty_coffee = Coffee("Cappuccino")
    assert Customer.most_aficionado(empty_coffee) is None
    with pytest.raises(ValueError):
        Customer.most_aficionado("not a coffee")  # Invalid coffee