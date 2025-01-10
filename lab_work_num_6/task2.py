from zipapp import create_archive


class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f'{self.make}, {self.model}'


class Car(Vehicle):

    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f'{super().get_info()}, {self.fuel_type}'



car1 = Car('aa', 'bb', 'cc')
print(car1.get_info())