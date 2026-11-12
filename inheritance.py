class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print('Vehicle is moving')

    def stop(self):
        print('Vehicle is standing by')


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.number_of_wheels = number_of_wheels

class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels

car = Car('Ford', 'Focus', 2008, 4, 4)
bike = Bike('Honda', 'Scoopy', 2018, 4)

#Наследование заключается в том чтобы классы могли наследовать все свойсвта и методы класса родителя, 
# удобно создавать абстрактный класс родитель чтобы потом его немного его наскледовать конкретными случаями!
# + - удобно писать код и меньше объема получается!