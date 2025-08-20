class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2

    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")


leaf = TeaLeaf(2)
print(leaf.age)

# leaf.age = 6
# print(leaf.age)


"""

Vehicle Rental System------------------>
You are designing a Vehicle Rental System that tracks different types of vehicles and their components.

Tasks:

- Create a class Engine with an attribute horsepower and a method get_engine_info() that returns "150 HP Engine".
- Create class Vehicle
Attributes: brand, model, and an Engine object.
Class attribute: total_vehicles (increased by 1 each time a new vehicle is created).
Add a method get_details() returning brand, model, and engine info.
Add @staticmethod get_vehicle_type() → returns "Generic Vehicle".
Add @classmethod get_total_vehicles() → returns total number of vehicles.
Add a @property rental_price and corresponding setter that ensures the value is non-negative.-
- Create a Car class that inherits from Vehicle.
- Add an attribute seats.
- Override the get_details() method and use super() to include base details and append "Seats: X".

"""


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def get_engine_info(self):
        return f"{self.horsepower} HP Engine"


class Vehicle:
    total_vehicles = 0

    def __init__(self, brand, model, engine: Engine):
        self.brand = brand
        self.model = model
        self.engine = engine
        self._rental_price = 0
        Vehicle.total_vehicles += 1

    def get_details(self):
        return f"{self.brand} {self.model} - {self.engine.get_engine_info()}"

    @staticmethod
    def get_vehicle_type():
        return "Generic Vehicle"

    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles

    @property
    def rental_price(self):
        return self._rental_price

    @rental_price.setter
    def rental_price(self, price):
        if price < 0:
            raise ValueError("Rental price must be non-negative")
        self._rental_price = price


class Car(Vehicle):
    def __init__(self, brand, model, engine: Engine, seats):
        super().__init__(brand, model, engine)
        self.seats = seats

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details} - Seats: {self.seats}"


engine1 = Engine(150)
car1 = Car("Toyota", "Corolla", engine1, 5)
car1.rental_price = 2000

engine2 = Engine(200)
car2 = Car("Honda", "Civic", engine2, 4)
car2.rental_price = 2500

print(car1.get_details())
print("Price:", car1.rental_price)

print(car2.get_details())
print("Price:", car2.rental_price)

print("Total Vehicles:", Vehicle.get_total_vehicles())
print("Vehicle Type:", Vehicle.get_vehicle_type())
