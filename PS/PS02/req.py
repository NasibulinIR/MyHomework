import requests
import pprint

"""Задание 1: Получение данных
Импортируйте библиотеку requests.
Отправьте GET-запрос к открытому API (например, https://api.github.com) с параметром для поиска репозиториев с кодом html.
Распечатайте статус-код ответа.
Распечатайте содержимое ответа в формате JSON."""

response = requests.get('https://api.github.com/search/repositories', params={'q':'HTML'})
response_json = response.json()
print(f'Задание 1: {response.status_code}')
# если нужен полный  json ---> print(response_json)
pprint.pprint(f'Общее количество репозиториев с использованием HTML: {response_json['total_count']}')

"""Задание 2: Параметры запроса
Используйте API, который позволяет фильтрацию данных через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
Отправьте GET-запрос с параметром userId, равным 1.
Распечатайте полученные записи."""
response_2 = requests.get('https://jsonplaceholder.typicode.com/posts?userId=1')
print(f'Задание 2: {response_2.text}')

"""Задание 3: Отправка данных
Используйте API, которое принимает POST-запросы для создания новых данных (например, https://jsonplaceholder.typicode.com/posts).
Создайте словарь с данными для отправки (например, {'title': 'foo', 'body': 'bar', 'userId': 1}).
Отправьте POST-запрос с этими данными.
Распечатайте статус-код и содержимое ответа."""

url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
response_3 = requests.post(url,json=data)
print(f'Задание 3:\n Статус-код: {response_3.status_code}')
print(f'Ответ - {response_3.json()}')
