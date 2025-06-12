def save_zoo(zoo, filename="zoo.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for animal in zoo.animals:
            file.write(f"animal,{animal.__class__.__name__},{animal.name},{animal.age}\n")

        for employee in zoo.employees:
            file.write(f"employee,{employee.name},{employee.position}\n")


def load_zoo(zoo_class, filename="zoo.txt"):
    zoo = zoo_class()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(',')
                if parts[0] == 'animal':
                    _load_animal(zoo, parts)
                elif parts[0] == 'employee':
                    _load_employee(zoo, parts)
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создан новый зоопарк.")
    return zoo

# Вспомогательная функция для загрузки животных
def _load_animal(zoo, parts):
    class_name, name, age = parts[1], parts[2], int(parts[3])
    if class_name == 'Bird':
        zoo.add_bird(name, age)
    elif class_name == 'Mammal':
        zoo.add_mammal(name, age)
    elif class_name == 'Reptile':
        zoo.add_reptile(name, age)
# Вспомогательная функция для загрузки персонала
def _load_employee(zoo, parts):
    name, position = parts[1], parts[2]
    zoo.add_employee(name, position)