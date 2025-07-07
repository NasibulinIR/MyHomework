from abc  import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    def __str__(self):
        return  getattr(self, 'name', self.__class__.__name__)

class Sword(Weapon):
    def __init__(self, name="меч"):
        self.name = name

    def attack(self):
        return 10

class Bow(Weapon):
    def __init__(self, name="лук"):
        self.name = name

    def attack(self):
        return 7

class Fighter():
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def attack(self, target):
        damage = self.weapon.attack()
        print(f'{self.name} атакует используя {self.weapon} и наносит {damage} урона')
        target.take_damage(damage)

    def change_weapon(self, new_weapon):
        old_weapon = self.weapon
        self.weapon = new_weapon
        print(f'{self.name} меняет оружие на {self.weapon}')

class Monster():
    def __init__(self, name, health=25):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f'{self.name} умирает')
        else:
            print(f'У {self.name.lower()}а осталось {self.health} здоровья')


if __name__ == '__main__':
    sword = Sword()
    bow = Bow()
    fighter = Fighter("Леха", bow)
    monster = Monster("Гоблин", health=25)

    fighter.attack(monster)
    fighter.attack(monster)
    fighter.change_weapon(sword)
    fighter.attack(monster)
    fighter.attack(monster)

