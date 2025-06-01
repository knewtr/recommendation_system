# Проект системы рекомендаций на основе графов
## Описание:
Данный проект представляет собой систему рекомендаций, основанной на алгоритмах PageRank и k-nearest-neighbours
## Содержание проекта:
* API для управления пользователями, книгами, взаимосвязями, рекомендациями
* Веб-интерфейс для получения данных
## Требования:
* Python 3.11 и выше
* PostgreSQL
* Redis
* Зависимости из requirements.txt
## Запуск проекта:
1. Склонируйте репозиторий
```
git clone https://github.com/knewtr/recommendation_system
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
3. Создайте файл .env в корне проекта и добавьте в него переменные окружения аналогично файлу .env.sample
```
SECRET_KEY=your_key

POSTGRES_DB=db_name
POSTGRES_USER=db_user
POSTGRES_PASSWORD=db_password
POSTGRES_HOST=db_host
POSTGRES_PORT=5432

LOCATION=redis://127.0.0.1:6379/1
```
4. Установите и запустите Redis
```
redis-server.exe
```
После запуска главная страница будет доступна по этому адресу http://localhost:8000/

## Визуализация графов
Для визуализации выполните команду:
```
python visualization.py
```
