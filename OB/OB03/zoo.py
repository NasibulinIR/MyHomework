from save_load_module import save_zoo, load_zoo
from animals import Bird, Mammal, Reptile
from employee import Employee, ZooKeeper, Veterinarian

class Zoo:
    def __init__(self):
        self.employees = []
        self.animals = []

    def add_bird(self, name, age, species):
        self.animals.append(Bird(name, age, species))

    def add_mammal(self, name, age, genus):
        self.animals.append(Mammal(name, age, genus))

    def add_reptile(self, name, age, color_species):
        self.animals.append(Reptile(name, age, color_species))

    def add_employee(self, name, position):
        employee = Employee(name, position)
        self.employees.append(employee)

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

my_zoo = Zoo()
load_zoo(my_zoo)
my_zoo.add_bird('Кеша',1, 'Попугай')
my_zoo.add_mammal('Мурка',7, 'Кошка')
my_zoo.add_reptile('Аркадий',4, 'Зеленый крокодил')
my_zoo.add_bird('Чижик',3, 'Стриж')

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

