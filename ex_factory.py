"""
Example of Factory pattern:
This example demonstrates the Factory pattern for creating different car models.
The factory produces instances of various subclasses of Car based on the user's choice.
The user can choose a car model from a list, and the factory assigns predefined specifications
such as horsepower, weight, and price.
"""

from abc import ABC, abstractmethod

# Define the Car abstract base class
class Car(ABC):
    @abstractmethod
    def get_model(self):
        pass

    @abstractmethod
    def get_specs(self):
        pass

# Define concrete Car classes
class Sedan(Car):
    def __init__(self):
        self.model = "Sedan"
        self.horsepower = 150
        self.weight = 1500
        self.price = 30000

    def get_model(self):
        return self.model

    def get_specs(self):
        return {
            "Model": self.model,
            "Horsepower": self.horsepower,
            "Weight": self.weight,
            "Price": self.price
        }

class SUV(Car):
    def __init__(self):
        self.model = "SUV"
        self.horsepower = 200
        self.weight = 2000
        self.price = 40000

    def get_model(self):
        return self.model

    def get_specs(self):
        return {
            "Model": self.model,
            "Horsepower": self.horsepower,
            "Weight": self.weight,
            "Price": self.price
        }

class SportsCar(Car):
    def __init__(self):
        self.model = "Sports Car"
        self.horsepower = 300
        self.weight = 1200
        self.price = 60000

    def get_model(self):
        return self.model

    def get_specs(self):
        return {
            "Model": self.model,
            "Horsepower": self.horsepower,
            "Weight": self.weight,
            "Price": self.price
        }

class Hatchback(Car):
    def __init__(self):
        self.model = "Hatchback"
        self.horsepower = 120
        self.weight = 1300
        self.price = 25000

    def get_model(self):
        return self.model

    def get_specs(self):
        return {
            "Model": self.model,
            "Horsepower": self.horsepower,
            "Weight": self.weight,
            "Price": self.price
        }

class Convertible(Car):
    def __init__(self):
        self.model = "Convertible"
        self.horsepower = 250
        self.weight = 1400
        self.price = 50000

    def get_model(self):
        return self.model

    def get_specs(self):
        return {
            "Model": self.model,
            "Horsepower": self.horsepower,
            "Weight": self.weight,
            "Price": self.price
        }

class PickupTruck(Car):
    def __init__(self):
        self.model = "Pickup Truck"
        self.horsepower = 180
        self.weight = 2200
        self.price = 35000

    def get_model(self):
        return self.model

    def get_specs(self):
        return {
            "Model": self.model,
            "Horsepower": self.horsepower,
            "Weight": self.weight,
            "Price": self.price
        }

# Define the CarFactory class
class CarFactory:
    @staticmethod
    def get_car(car_model):
        if car_model == "Sedan":
            return Sedan()
        elif car_model == "SUV":
            return SUV()
        elif car_model == "Sports Car":
            return SportsCar()
        elif car_model == "Hatchback":
            return Hatchback()
        elif car_model == "Convertible":
            return Convertible()
        elif car_model == "Pickup Truck":
            return PickupTruck()
        else:
            return None

# Function to display car models and get user choice
def choose_car_model():
    car_models = ["Sedan", "SUV", "Sports Car", "Hatchback", "Convertible", "Pickup Truck"]
    print("\nAvailable Car Models:")
    for i, model in enumerate(car_models, 1):
        print(f"{i}. {model}")

    choice = int(input("Choose a car model by entering the corresponding number: "))
    return car_models[choice - 1]

# Usage
if __name__ == "__main__":
    car_factory = CarFactory()

    while True:
        print("\n--- Car Factory ---")
        car_model = choose_car_model()
        car = car_factory.get_car(car_model)
        
        if car:
            specs = car.get_specs()
            print("\nCar Specifications:")
            for key, value in specs.items():
                print(f"{key}: {value}")
        else:
            print("Unknown car model selected.")

        another = input("\nDo you want to choose another car model? (yes/no): ").lower()
        if another != 'yes':
            print("Exiting the Car Factory.")
            break
