class Car:
    def __init__(self, brand, model, year, number_of_wheels):
        self.brand = brand
        self.model = model
        self.year = year
        self.number_of_wheels = number_of_wheels

    def start(self):
        print('Car is moving')

    def stop(self):
        print('Car is standing by')

class Motorcycle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print('Motorcycle is moving')

    def stop(self):
        print('Motorcycle is standing by')

class People:
    def __init__(self, age):
        self.age = age

vehicles = [
    Car('Ford', 'Focus', 2008, 5),
    Motorcycle('Honda', 'Scoopy', 2018)
]

for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f'Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})')
        vehicle.start()
        vehicle.stop()
    elif isinstance(vehicle, Motorcycle):
        print(f'Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})')
        vehicle.start()
        vehicle.stop()
    else:
        raise Exception('The object is not a vehicle')

#Полиморфмизм состоит в том чтобы исопльзовать одни и те же методы разных классов по одинаково но с небольшими своими изменениями, 
# не обязатеньно наследовать!
#+ - удобство в создании новых классов с уже знакомыми методами!
    