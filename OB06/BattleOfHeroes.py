import random

# Создание базового персонажа
class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.weapon = None

    def attack(self, other):
        damage = self.attack_power
        if self.weapon:
            damage = self.weapon.calculate_damage(self.attack_power)
        other.health -= damage
        print(f"{self.name} атаковал {other.name} и нанес {damage} урона.")

    def is_alive(self):
        return self.health > 0

# Создание классов персонажей
class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=15)

class Mage(Hero):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=25)

class Thief(Hero):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=20)

# Создание базового оружия
class Weapon:
    def __init__(self, name):
        self.name = name

    def calculate_damage(self, base_damage):
        return base_damage

# Создание классов оружий
class Sword(Weapon):
    def __init__(self):
        super().__init__("Меч")

    def calculate_damage(self, base_damage):
        return base_damage + 5

class Staff(Weapon):
    def __init__(self):
        super().__init__("Посох")

    def calculate_damage(self, base_damage):
        return base_damage + 10

class Bow(Weapon):
    def __init__(self):
        super().__init__("Лук")

    def calculate_damage(self, base_damage):
        if random.random() < 0.3:  # 30% шанс на критический урон
            return base_damage * 2
        return base_damage

# Создание класса игры
class Game:
    def __init__(self, player_name, player_class, player_weapon):
        self.player = player_class(player_name)
        self.player.weapon = player_weapon()
        self.computer_class = random.choice([Warrior, Mage, Thief])
        self.computer = self.computer_class("Типичный злодей")
        self.computer.weapon = self.get_computer_weapon(self.computer_class)

    def get_computer_weapon(self, computer_class):
        # Выбор оружия в зависимости от класса компьютера
        if computer_class == Warrior:
            return Sword()
        elif computer_class == Mage:
            return Staff()
        else:
            return Bow()

    def start(self):
        print("Начало игры!")
        if self.player.__class__.__name__ == "Warrior":
            print(f"Ваш персонаж: {self.player.name}, класс: Воин, оружие: {self.player.weapon.name}")
        elif self.player.__class__.__name__ == "Mage":
            print(f"Ваш персонаж: {self.player.name}, класс: Маг, оружие: {self.player.weapon.name}")
        else:
            print(f"Ваш персонаж: {self.player.name}, класс: Вор, оружие: {self.player.weapon.name}")

        if self.computer.__class__.__name__ == "Warrior":
            print(f"Противник: {self.computer.name}, класс: Воин, оружие: {self.computer.weapon.name}")
        elif self.computer.__class__.__name__ == "Mage":
            print(f"Противник: {self.computer.name}, класс: Маг, оружие: {self.computer.weapon.name}")
        else:
            print(f"Противник: {self.computer.name}, класс: Вор, оружие: {self.computer.weapon.name}")

        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} побежден!")
                break
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.\n")

            # Ход компьютера
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} побежден!")
                break
            print(f"У {self.player.name} осталось {self.player.health} здоровья.\n")

        print("Игра завершена.")

if __name__ == "__main__":
    # Выбор персонажа и оружия
    player_name = input("Введите имя вашего героя: ")
    print("Выберите класс персонажа:")
    print("1. Воин")
    print("2. Маг")
    print("3. Вор")
    player_class_choice = input("Введите номер класса (1-3): ")
    player_class = [Warrior, Mage, Thief][int(player_class_choice) - 1]

    # Выбор оружия в зависимости от класса
    if player_class == Warrior:
        player_weapon = Sword
    elif player_class == Mage:
        player_weapon = Staff
    else:
        player_weapon = Bow

    game = Game(player_name, player_class, player_weapon)
    game.start()