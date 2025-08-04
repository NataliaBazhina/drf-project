# LMS-система

LMS-система - это веб-приложение, позволяющее пользователям размещать свои полезные материалы или курсы.

## Описание

LMS-система позволяет создавать и управлять курсами, добавлять материалы, а также предоставляет функционал для управления пользователями и их доступами.

## Авторы

* Имя: Бажина Наталья
* Email: nataliaagapova27@yandex.ru
* GitHub: https://github.com/NataliaBazhina

## Требования к проекту

* Python: версия 3.8 или выше
* Django: версия 3.2 или выше
* PostgreSQL: версия 12 или выше
* Docker: версия 20.10 или выше
* Docker Compose: версия 2.0 или выше

## Инструкции по установке и запуску проекта

### Локальная установка (без Docker)

1. Клонировать репозиторий: `git clone git@github.com:NataliaBazhina/drf-project.git`
2. Перейти в папку проекта: `cd project`
3. Установить зависимости: `pip install -r requirements.txt`
4. Создайте файл `.env` в корневой папке проекта и заполните его по шаблону `.env.sample` переменными:
   - `SECRET_KEY`: секретный ключ проекта (например, случайная строка из 50 символов)
   - `NAME`: имя базы данных
   - `DBUSER`: имя пользователя базы данных
   - `PASSWORD`: пароль пользователя базы данных
   - `HOST`: адрес хоста базы данных (например, localhost)
   - `PORT`: порт базы данных (например, 5432)
5. Создать базу данных: `python manage.py migrate`
6. Запустить сервер: `python manage.py runserver`

### Запуск через Docker Compose

1. Клонировать репозиторий: `git clone git@github.com:NataliaBazhina/drf-project.git`
2. Перейти в папку проекта: `cd project`
3. Создать файл `.env` на основе `.env.sample` 
4. Запустить проект: `docker-compose up -d --build`
5. Проект будет доступен по адресу: http://localhost:8080

## Проверка работоспособности сервисов

1. **Django-приложение (web)**:
   - Откройте в браузере: http://localhost:8080
   - Проверка логов: `docker-compose logs web`

2. **PostgreSQL (db)**:
   - Проверить подключение: `docker-compose exec db psql -U postgres -d drf`
   - Проверка логов: `docker-compose logs db`

3. **Redis**:
   - Проверить работу: `docker-compose exec redis redis-cli ping` (должен ответить "PONG")
   - Проверка логов: `docker-compose logs redis`

4. **Celery (worker)**:
   - Проверка логов: `docker-compose logs celery`

5. **Celery Beat (scheduler)**:
   - Проверка логов: `docker-compose logs celery_beat`

## Остановка проекта

Для остановки всех сервисов выполните:
`docker-compose down`

Для полной очистки (с удалением volumes):
`docker-compose down -v`