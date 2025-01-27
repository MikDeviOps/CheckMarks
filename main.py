from pathlib import Path

import requests

# URL
url = "http://127.0.0.1:5995/api/v1/stats"

# Заголовки запроса
headers = {
    "Content-Type": "application/json",
    "Authorization": "Basic"
}

# Выполнение GET-запроса с указанными заголовками
response = requests.get(url, headers=headers)

# Проверка статуса-кода ответа
if response.status_code == 200:
    # Парсинг JSON из ответа
    response_data = response.json()

    # Кол-во обращений к API - Статусы и ошибки.
    api_status_code_200 = response_data['api']['status_code']['200']['value']
    api_status_code_400 = response_data['api']['status_code']['400']['value']
    api_status_code_500 = response_data['api']['status_code']['500']['value']
    api_status_code_503 = response_data['api']['status_code']['503']['value']

    # Запрос инициализации модуля
    api_successful_init = response_data['core']['successful_init']['value']

    # Запрос версии модуля
    api_system_version = response_data['system']['software']['version']['value']

    # Запрос кол-во операций с документами
    api_status_docs_p = response_data['yenisei']['docs']['purged']['value']
    api_status_docs_d = response_data['yenisei']['docs']['deleted']['value']
    api_status_docs_a = response_data['yenisei']['docs']['added']['value']

    # Сохранение данных в текстовый файл
    log_file_path = Path('D:/api_stats.txt')

    # Запись в тхт файл данные по запросам.
    with log_file_path.open('w') as file:
        file.write(f"Кол-во обращений к API: {api_status_code_200}\n")
        file.write(f"Кол-во ошибок 400: {api_status_code_400}\n")
        file.write(f"Кол-во ошибок 500: {api_status_code_500}\n")
        file.write(f"Кол-во ошибок 503: {api_status_code_503}\n")
        file.write(f"Успешная инициализация модуля: {api_successful_init}\n")
        file.write(f"Версия ЛМЧЗ: {api_system_version}\n")
        file.write(f"Запрос кол-во операций с документами - Добавлено: {api_status_docs_a}\n")
        file.write(f"Запрос кол-во операций с документами - Удалено: {api_status_docs_d}\n")
        file.write(f"Запрос кол-во операций с документами - Очищено: {api_status_docs_p}\n")

    print("Данные успешно сохранены в файл")
else:
    print(f"Произошла ошибка: {response.status_code}")
    print(f"Сообщение: {response.text}")

'''
Result:

Кол-во обращений к API: 90
Кол-во ошибок 400: 3
Кол-во ошибок 500: 0
Кол-во ошибок 503: 0
Успешная инициализация модуля: 1
Версия ЛМЧЗ: 1.0.7-215
Запрос кол-во операций с документами - Добавлено: 25254
Запрос кол-во операций с документами - Удалено: 8
Запрос кол-во операций с документами - Очищено: 1561

'''