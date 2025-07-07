class User:
    def __init__(self, user_id : int, name: str):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

class Admin(User):
    def __init__(self, user_id : int, name : str):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._users = []

    def add_user (self, user):
        self._users.append(user)
        print(f"Пользователь {user.get_name()} добавлен в систему.")

    def remove_user(self, user_id):
        for user in self._users:
            if user.get_user_id() == user_id:
                self._users.remove(user)
                print(f"Пользователь {user.get_name()} удален из системы.")
                return

    def list_users(self):
        print('\nСписок пользователей:')
        for user in self._users:
            print(f"ID: {user.get_user_id()}, Имя: {user.get_name()}, Уровень доступа: {user.get_access_level()}")

admin1 = Admin(1, 'Admin')

user1 = User(2, 'SimpleUser')
user2 = User(3, 'CommonUser')
user3 = User(4, 'UncommonUser')

admin1.add_user(admin1)
admin1.add_user(user1)
admin1.add_user(user2)
admin1.add_user(user3)
print(user1.get_name())

admin1.remove_user(4)

admin1.list_users()
