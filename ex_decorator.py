"""
Example of Decorator pattern:
This example demonstrates the Decorator pattern by creating a Coffee Ordering System.
Different types of additions (Milk, Sugar, Chocolate) are added dynamically to a basic Coffee order.
"""

from abc import ABC, abstractmethod

# Basic Coffee class
class Coffee:
    def cost(self):
        return 5.00  # Base cost of the coffee

    def description(self):
        return "Basic Coffee"

# Abstract Decorator class
class CoffeeDecorator(ABC):
    def __init__(self, coffee):
        self._coffee = coffee

    @abstractmethod
    def cost(self):
        pass

    @abstractmethod
    def description(self):
        pass

# Concrete Decorator for Milk
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.50

    def description(self):
        return f"{self._coffee.description()} + Milk"

# Concrete Decorator for Sugar
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.25

    def description(self):
        return f"{self._coffee.description()} + Sugar"

# Concrete Decorator for Chocolate
class ChocolateDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 0.75

    def description(self):
        return f"{self._coffee.description()} + Chocolate"

# Function to interact with the coffee ordering system
def interactive_coffee_order():
    coffee = Coffee()
    while True:
        print(f"\nCurrent Order: {coffee.description()}")
        print(f"Current Cost: ${coffee.cost():.2f}")
        print("\nAdditions:")
        print("1. Milk ($0.50)")
        print("2. Sugar ($0.25)")
        print("3. Chocolate ($0.75)")
        print("4. Checkout")
        choice = input("Choose an addition by entering the corresponding number: ")

        if choice == "1":
            coffee = MilkDecorator(coffee)
        elif choice == "2":
            coffee = SugarDecorator(coffee)
        elif choice == "3":
            coffee = ChocolateDecorator(coffee)
        elif choice == "4":
            print("\nFinal Order:")
            print(f"Description: {coffee.description()}")
            print(f"Total Cost: ${coffee.cost():.2f}")
            break
        else:
            print("Invalid choice, please try again.")

# Usage
if __name__ == "__main__":
    interactive_coffee_order()
