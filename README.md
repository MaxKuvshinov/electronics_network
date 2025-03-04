# Electronics Network API

## Описание проекта.

Electronics Network API — это RESTful API для управления сетью по продаже электроники, разработанное с использованием Django и Django REST Framework (DRF). 
Проект поддерживает иерархическую структуру участников сети (заводы, розничные сети, индивидуальные предприниматели) и связанных с ними продуктов, а также управление пользователями с JWT-аутентификацией.

### Проект разделен на три основных приложения:
1. `users`: Управление пользователями (CustomUser) с ролями и аутентификацией через JWT.
2. `product`: Управление продуктами (Product), связанными с участниками сети.
3. `network`: Управление участниками сети (NetworkNode) с трёхуровневой иерархией.

## Технические требования
- Python 3.8+
- Django 3+
- DRF 3.10+
- PostgreSQL 10+
- Swagger и Redoc /OpenAPI для документации

## Установка:
1. Клонируйте репозиторий
- `git@github.com:MaxKuvshinov/electronics_network.git`

2. Создайте виртуальное окружение:
- `python -m venv venv`

3. Активируйте виртуальное окружение:
- `venv\Scripts\activate` - для Windows
- `source venv/bin/activate` - для macOS/Linux

4. Установите зависимости
- `pip install -r requirements.txt`   

5. Создайте файл .env на основе .env.sample
- `SECRET_KEY=`
- `DEBUG=`
- `POSTGRES_DB=`
- `POSTGRES_USER=`
- `POSTGRES_PASSWORD=`
- `POSTGRES_HOST=`
- `POSTGRES_PORT=`

6. Примените миграции:
- `python manage.py makemigrations`
- `python manage.py migrate`

7. Создайте суперпользователя:
- `python manage.py createsuperuser_custom --email youemail --password youpassword`

## Запуск проекта
1. Запустите сервер
- `python manage.py runserver`
2. Тестирование 
- Используйте Postman для отправки запросов к API.

## Документация
- Для Swagger UI - `http://127.0.0.1:8000/swagger/`
- Для Redoc - `http://127.0.0.1:8000/redoc/`

