import requests
import json

# Базовый URL вашего API
BASE_URL = 'http://localhost:8000/api/'

def get_data():
    """Функция для получения данных"""
    response = requests.get(f'{BASE_URL}get_data/')
    if response.status_code == 200:
        print("Получены данные:")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Ошибка при получении данных: {response.status_code}")

def write_data(token, title):
    """Функция для записи данных"""
    data = {
        'token': token,
        'title': title
    }
    response = requests.post(f'{BASE_URL}write_data/', json=data)
    if response.status_code == 201:
        print("Данные успешно записаны:")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Ошибка при записи данных: {response.status_code}")
        print(response.text)

# Проверка получения данных
print("Проверка получения данных:")
get_data()

# Проверка записи данных
print("\nПроверка записи данных:")
write_data("test_token", "Test Title")

# Повторная проверка получения данных после записи
print("\nПовторная проверка получения данных:")
get_data()