class Animal:
    animals = []

    def __init__(self, name, sound, weight):
        self.name = name
        self.sound = sound
        self.weight = weight
        self.animals.append(self)

    def feed(self):
        print(f'{self.name} накормлен(а)')


class Bird(Animal):
    def collect_eggs(self):
        print(f'Яйца {self.name} собраны')


class Cattle(Animal):
    def milk(self):
        print(f'{self.name} подоена')


class Sheep(Animal):
    def shear(self):
        print(f'{self.name} подстрижен(а)')


class Cow(Cattle):
    pass


class Goat(Cattle):
    pass


class Goose(Bird):
    pass


class Chicken(Bird):
    pass


class Duck(Bird):
    pass
