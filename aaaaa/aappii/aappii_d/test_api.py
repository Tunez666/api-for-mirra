import requests
import json
import uuid

BASE_URL = 'http://localhost:8000/api/arrr/'  # Исправленный URL

def get_token():
    """Функция получения JWT-токена"""
    data = {
        "username": "br",  # Проверь, что логин правильный
        "password": "1"  # Проверь, что пароль правильный
    }
    response = requests.post("http://localhost:8000/api/token/", json=data)
    if response.status_code == 200:
        return response.json()["access"]
    else:
        print("Ошибка получения токена:", response.json())
        return None

def get_data(token):
    """Запрос данных с авторизацией"""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f'{BASE_URL}', headers=headers)  # Убрали `get_data/`, т.к. он в ViewSet
    if response.status_code == 200:
        print("Полученные данные:", response.json())
    else:
        print("Ошибка при получении данных:", response.text)

def write_data(token, title):
    """Добавляем новую запись"""
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        'token': str(uuid.uuid4()),  # Генерируем случайный токен
        'title': title
    }
    response = requests.post(f'{BASE_URL}', json=data, headers=headers)  # Убрали `write_data/`
    if response.status_code == 201:
        print("Запись успешно создана:", response.json())
    else:
        print("Ошибка при записи данных:", response.text)

# Получаем токен
jwt_token = get_token()
if jwt_token:
    print("✅ Токен получен")
    get_data(jwt_token)  # Теперь запросы идут с токеном
    write_data(jwt_token, "Тестовая запись")
