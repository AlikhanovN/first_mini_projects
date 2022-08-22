class Car:
    def __init__(self, make, model, year, odometer = 0, fuel = 70):
        self.make = make
        self.model = model
        self.year = year
        self.odometr = odometer
        self.fuel = fuel

    def drive(self):
        road = int(input("Enter km: "))
        self.validator_drive(road)
        self.road = road

    def __add_distance(self):
        self.odometr += self.road

    def __subtract_fuel(self):
        self.fuel -= self.road / 10

    def validator_drive(self, km):
        if km > 700:
            raise ValueError("Need more fuel, please, fill more!")

    def __str__(self):
        self.drive()
        self.__add_distance()
        self.__subtract_fuel()
        return f"Let’s drive! Fuel left = {self.fuel}"

mers = Car("Mers", "c300", "2016")
print(mers)
