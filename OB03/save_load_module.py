from animals import Bird, Mammal, Reptile
def save_zoo(zoo, filename="zoo.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for animal in zoo.animals:
            line = f"animal,{animal.__class__.__name__},{animal.name},{animal.age}"

            if isinstance(animal, Bird):
                line += f',{animal.species}'
            elif isinstance(animal, Mammal):
                line += f',{animal.genus}'
            elif isinstance(animal, Reptile):
                line += f',{animal.color_species}'

            file.write(line + "\n")

        for employee in zoo.employees:
            file.write(f"employee,{employee.name},{employee.position}\n")


def load_zoo(zoo_instance, filename="zoo.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(',')
                if parts[0] == 'animal':
                    _load_animal(zoo_instance, parts)
                elif parts[0] == 'employee':
                    _load_employee(zoo_instance, parts)
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создан новый зоопарк.")
    return zoo_instance

# Вспомогательная функция для загрузки животных
def _load_animal(zoo, parts):
    class_name, name, age, = parts[1], parts[2], int(parts[3])
    if class_name == 'Bird' and len(parts) == 5:
        zoo.add_bird(name, age, parts[4])
    elif class_name == 'Mammal' and len(parts) == 5:
        zoo.add_mammal(name, age, parts[4])
    elif class_name == 'Reptile' and len(parts) == 5:
        zoo.add_reptile(name, age, parts[4])
# Вспомогательная функция для загрузки персонала
def _load_employee(zoo, parts):
    name, position = parts[1], parts[2]
    zoo.add_employee(name, position)
