class Vehicle():
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def __init__(self, capacity = 50):
        self.capacity = capacity
    def seating_capacity(self):
        return f"The seating capacity of a Bus is {self.capacity} passengers"

a = Vehicle("Frog", 220, 123123)
print(a.seating_capacity(100))
b = Bus()
print(b.seating_capacity())
