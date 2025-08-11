# LMS-система

LMS-система - это веб-приложение, позволяющее пользователям размещать свои полезные материалы или курсы.

## Описание

LMS-система позволяет создавать и управлять курсами, добавлять материалы, а также предоставляет функционал для управления пользователями и их доступами.

## Автор

* Имя: Бажина Наталья
* Email: nataliaagapova27@yandex.ru
* GitHub: https://github.com/NataliaBazhina

## Технологии

- Python 3.10
- Django 4.2
- PostgreSQL 14
- Docker 20.10+
- GitHub Actions

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

### Production-развертывание 

1. Подготовка сервера

sudo apt update
sudo apt install docker.io
sudo systemctl enable docker

2. Настройка переменных окружения

mkdir -p ~/drf-project
nano ~/drf-project/.env  # скопируйте переменные из .env.sample

3. Создание systemd сервиса
sudo nano /etc/systemd/system/myapp.service
Вставьте:

[Unit]
Description=Django LMS Application
After=network.target docker.service

[Service]
Type=simple
Restart=always
RestartSec=5s
EnvironmentFile=/etc/default/myapp
ExecStart=/usr/bin/docker run \
  --name myapp \
  -p 80:8080 \
  -e HOST=localhost \
  -v /home/ubuntu/drf-project/.env:/app/.env \
  ${DOCKER_IMAGE}
ExecStop=/usr/bin/docker stop myapp

[Install]
WantedBy=multi-user.target

4. Создание файла переменных образа
sudo nano /etc/default/myapp

Добавьте: DOCKER_IMAGE=your-dockerhub-username/myapp:latest

5. Активация сервиса  
sudo systemctl daemon-reload
sudo systemctl enable myapp.service
sudo systemctl start myapp.service

            CI/CD Pipeline

Автоматический деплой при push, pull_request:

Сборка Docker образа

Пуш в Docker Hub

Деплой на сервер через SSH

            Необходимые Secrets:

DOCKER_HUB_USERNAME

DOCKER_HUB_TOKEN

SSH_KEY

SERVER_IP

