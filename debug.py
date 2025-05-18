from customer import Customer
from coffee import Coffee
from order import Order

def main():
    # Create customers
    try:
        alice = Customer("Alice")
        bob = Customer("Bob")
    except ValueError as e:
        print(f"Error creating customer: {e}")
        return

    # Create coffees
    try:
        latte = Coffee("Latte")
        espresso = Coffee("Espresso")
    except ValueError as e:
        print(f"Error creating coffee: {e}")
        return

    # Create orders
    try:
        alice.create_order(latte, 5.0)
        alice.create_order(espresso, 3.5)
        bob.create_order(latte, 4.5)
        bob.create_order(latte, 5.0)
    except ValueError as e:
        print(f"Error creating order: {e}")
        return

    # Test relationships
    print(f"Alice's orders: {len(alice.orders())}")
    print(f"Latte's customers: {[c.name for c in latte.customers()]}")
    print(f"Latte's average price: {latte.average_price():.2f}")
    
    # Test most_aficionado
    aficionado = Customer.most_aficionado(latte)
    print(f"Most aficionado for Latte: {aficionado.name if aficionado else 'None'}")

if __name__ == "__main__":
    main()