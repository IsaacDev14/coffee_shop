
# Coffee Shop Order Management System

This is a simple Python project modeling a coffee shop order management system. It demonstrates object-oriented programming concepts including classes, properties, validation, and relationships between entities.

## Project Overview

The system consists of three main classes:

- **Customer**: Represents a customer with validation on the name, manages orders and coffees purchased.
- **Coffee**: Represents a coffee type with name validation and tracks related orders and customers.
- **Order**: Represents an order linking a customer, coffee, and price, with input validation.

## Features

- Validation on all entities (Customer names, Coffee names, Order prices).
- Bidirectional relationships:
  - Customers can retrieve their orders and coffees.
  - Coffees can retrieve their orders and customers.
- Ability to find the "most aficionado" customer who spent the most on a particular coffee.
- Comprehensive unit tests covering all key functionalities.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/coffee-shop.git
   cd coffee-shop
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies (if any):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

You can run the `debug.py` script to see a simple demonstration of the system:

```bash
python debug.py
```

## Testing

The project uses `pytest` for testing. To run all tests, make sure you set the `PYTHONPATH` to the project root:

```bash
PYTHONPATH=. pytest
```

To run specific test files, e.g., for customers:

```bash
PYTHONPATH=. pytest tests/test_customer.py
```

## File Structure

```
.
├── coffee.py        # Coffee class implementation
├── customer.py      # Customer class implementation
├── order.py         # Order class implementation
├── debug.py         # Demonstration script
├── tests/           # Unit tests for all classes
│   ├── test_coffee.py
│   ├── test_customer.py
│   └── test_order.py
├── README.md        # Project documentation
```

## Contributing

Feel free to fork this repository and submit pull requests. Please write tests for any new features or bug fixes.

## License

This project is licensed under the MIT License.

---

**Author:** Isaac Mwiti Kubai  
**Date:** 2025-05-18
