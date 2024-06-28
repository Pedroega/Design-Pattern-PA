"""
Example of Observer pattern:
This example demonstrates the Observer pattern in a stock monitoring system. The Stock (Subject) notifies
different components (Observers) like Store and Warehouse when the stock quantity of a product is updated.
The user can interactively add products, update stock quantities, and see notifications in real-time.
"""

# Define the Observer abstract base class
class Observer:
    def update(self, product_name, quantity):
        pass

# Define a concrete Observer for a Store
class Store(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, product_name, quantity):
        print(f"Store {self.name} notified: {product_name} stock updated to {quantity} units.")

# Define a concrete Observer for a Warehouse
class Warehouse(Observer):
    def __init__(self, location):
        self.location = location

    def update(self, product_name, quantity):
        print(f"Warehouse at {self.location} notified: {product_name} stock updated to {quantity} units.")

# Define the Subject class
class Stock:
    def __init__(self):
        self.observers = []
        self.products = {}

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, product_name):
        for observer in self.observers:
            observer.update(product_name, self.products[product_name])

    def update_stock(self, product_name, quantity):
        self.products[product_name] = quantity
        self.notify_observers(product_name)

    def add_product(self, product_name, initial_quantity):
        self.products[product_name] = initial_quantity
        self.notify_observers(product_name)

# Function to interact with the stock system
def interactive_stock_system():
    stock = Stock()
    
    # Create observers
    store1 = Store("Main Street")
    store2 = Store("Second Avenue")
    warehouse = Warehouse("Central Warehouse")
    
    # Register observers with the stock
    stock.add_observer(store1)
    stock.add_observer(store2)
    stock.add_observer(warehouse)
    
    while True:
        print("\n--- Stock Management System ---")
        print("1. Add Product")
        print("2. Update Stock")
        print("3. Show Products")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            product_name = input("Enter product name: ")
            initial_quantity = int(input("Enter initial quantity: "))
            stock.add_product(product_name, initial_quantity)
        elif choice == "2":
            product_name = input("Enter product name: ")
            if product_name in stock.products:
                quantity = int(input("Enter new quantity: "))
                stock.update_stock(product_name, quantity)
            else:
                print(f"Product '{product_name}' does not exist.")
        elif choice == "3":
            print("\nCurrent Products and Quantities:")
            for product, quantity in stock.products.items():
                print(f"{product}: {quantity} units")
        elif choice == "4":
            print("Exiting the system.")
            break
        else:
            print("Invalid option. Please try again.")

# Usage
if __name__ == "__main__":
    interactive_stock_system()
