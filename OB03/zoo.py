from save_load_module import save_zoo, load_zoo

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat (self):
        pass

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} радостно щебечет: Чирик-курлык")

    def eat(self):
        print(f"{self.name} клюет зерно")

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} протяжно мяукает: Мяу-мяу")

    def eat(self):
        print(f"{self.name} ест мясо")

class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} производит звук: Шш-шш-шш")

    def eat(self):
        print(f"{self.name} ест рыбу")

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"\n{self.name} кормит {animal.name}")

class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"\n{self.name} лечит {animal.name}")

class Zoo:
    def __init__(self):
        self.employees = []
        self.animals = []

    def add_bird(self, name, age):
        self.animals.append(Bird(name, age))

    def add_mammal(self, name, age):
        self.animals.append(Mammal(name, age))

    def add_reptile(self, name, age):
        self.animals.append(Reptile(name, age))

    def add_employee(self, name, position):
        employee = Employee(name, position)
        self.employees.append(employee)

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

load_zoo(Zoo)

my_zoo = Zoo()
my_zoo.add_bird('Кеша',1)
my_zoo.add_mammal('Мурка',7)
my_zoo.add_reptile('Аркадий',4)
my_zoo.add_bird('Чижик',3)

my_zoo.add_employee('Василий Петрович', 'Ветеринар')
my_zoo.add_employee('Лариса Ивановна', 'Зоолог')
my_zoo.add_employee('Сергей Анатольевич', 'Завхоз')

veterinarian = Veterinarian('Василий Петрович', 'Ветеринар')
zookeeper = ZooKeeper('Лариса Ивановна', 'Зоолог')

animals = my_zoo.animals
animal_sound(animals)
veterinarian.heal_animal(my_zoo.animals[3])
zookeeper.feed_animal(my_zoo.animals[1])

save_zoo(my_zoo)
