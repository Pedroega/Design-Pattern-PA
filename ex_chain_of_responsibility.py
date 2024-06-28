"""
Example of Chain of Responsibility pattern:
This example demonstrates the Chain of Responsibility pattern by creating an Expense Approval System.
Different levels of authority (Employee, Manager, Director) handle expense approval based on the amount.
If a level cannot approve the expense, it passes the request to the next level.
"""

from abc import ABC, abstractmethod
import time

# Define the Handler abstract base class
class ExpenseHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next_handler(self, handler):
        self.next_handler = handler

    @abstractmethod
    def handle_expense(self, amount):
        pass

# Define a concrete Handler for Employee
class EmployeeHandler(ExpenseHandler):
    def handle_expense(self, amount):
        if amount <= 100:
            print("Employee: Approved expense of ${}".format(amount))
        elif self.next_handler:
            print("Employee: Cannot approve expense of ${}. Passing to the next handler...".format(amount))
            time.sleep(1)  # Add a delay of 1 second
            self.next_handler.handle_expense(amount)
        else:
            print("Employee: Cannot approve expense of ${}. No more handlers available.".format(amount))

# Define a concrete Handler for Manager
class ManagerHandler(ExpenseHandler):
    def handle_expense(self, amount):
        if amount <= 1000:
            print("Manager: Approved expense of ${}".format(amount))
        elif self.next_handler:
            print("Manager: Cannot approve expense of ${}. Passing to the next handler...".format(amount))
            time.sleep(1)  # Add a delay of 1 second
            self.next_handler.handle_expense(amount)
        else:
            print("Manager: Cannot approve expense of ${}. No more handlers available.".format(amount))

# Define a concrete Handler for Director
class DirectorHandler(ExpenseHandler):
    def handle_expense(self, amount):
        if amount <= 10000:
            print("Director: Approved expense of ${}".format(amount))
        elif self.next_handler:
            print("Director: Cannot approve expense of ${}. Passing to the next handler...".format(amount))
            time.sleep(1)  # Add a delay of 1 second
            self.next_handler.handle_expense(amount)
        else:
            print("Director: Cannot approve expense of ${}. No more handlers available.".format(amount))

# Function to interact with the expense approval system
def interactive_expense_approval_system():
    director_handler = DirectorHandler()
    manager_handler = ManagerHandler(director_handler)
    employee_handler = EmployeeHandler(manager_handler)

    while True:
        print("\n--- Expense Approval System ---")
        print("Enter the amount of expense or 'exit' to quit:")
        input_value = input("Expense amount: ")

        if input_value.lower() == "exit":
            print("Exiting the system.")
            break
        else:
            try:
                amount = float(input_value)
                employee_handler.handle_expense(amount)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

# Usage
if __name__ == "__main__":
    interactive_expense_approval_system()
