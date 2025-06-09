class Store:
    def __init__(self, name, address, items=None):
        if items is None:
            items = {}
        self.name = name
        self.address = address
        self.items = items

    def add_product(self, name, price):
        self.items[name] = price
        print(f"Товар '{name}' добавлен в ассортимент.")
        return self.items

    def remove_product(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Товар '{name}' удален из ассортимента.")
        return self.items

    def get_price(self, name):
        if name in self.items:
            return self.items[name]  # Возвращает только цену (число)
        else:
            return None  #

    def update_price(self, name, new_price):
        if name in self.items:
            self.items[name] = new_price
            print("Цена товара обновлена.")
            return self.items

    def current_assortment(self):
        print("Текущий ассортимент магазина:")
        for name, price in self.items.items():
            print(f"{name}: {price} руб.")
        return self.items

store1 = Store('Красный Яр', 'ул. Железнодорожников 8')
store2 = Store('Командор', 'ул. Менжинского 8')
store3 = Store('Пятерочка', 'пр. Красноярский Рабочий  162')

store1.add_product('Молоко', 100)
store1.add_product('Яблоки', 105)
store1.add_product('Бананы', 122)
store1.add_product('Помидоры', 235)

store1.update_price('Яблоки', 123)

store1.remove_product('Бананы')

print(store1.get_price('Яблоки'))
print(store1.current_assortment())

















