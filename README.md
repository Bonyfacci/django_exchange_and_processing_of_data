## Django-приложение, которое обрабатывает и анализирует чеки покупок

### Стек технологий:

 - ![alt text](https://img.shields.io/badge/Python-3.11.5-grey?style=plastic&logo=python&logoColor=white&labelColor=%233776AB)

 - ![alt text](https://img.shields.io/badge/Django-5.0.3-grey?style=plastic&logo=django&logoColor=white&labelColor=%23092E20)

 - ![alt text](https://img.shields.io/badge/PostgreSQL-15.3-grey?style=plastic&logo=postgresql&logoColor=white&labelColor=%234169E1)

 - ![alt text](https://img.shields.io/badge/Celery-5.3.6-grey?style=plastic&logo=celery&logoColor=white&labelColor=37814A)

 - ![alt text](https://img.shields.io/badge/Redis-5.0.2-grey?style=plastic&logo=redis&logoColor=white&labelColor=DC382D)

 - ![alt text](https://img.shields.io/badge/Kafka-5.0.2-grey?style=plastic&logo=kafka&logoColor=white&labelColor=white)


### Описание проекта
Целью данного проекта является создание двух сервисов, связанных посредством Apache Kafka, 
для обработки и анализа чеков покупок. Первый сервис отвечает за прием, валидацию и запись чеков в журнал, 
а также их передачу второму сервису. Второй сервис разбивает содержимое чеков на привязку к местам покупок, 
считает аналитику и предоставляет данные по API.

***

### Запуск через консоль

<details>
<summary>Для запуска через консоль необходимо:</summary>

- Клонировать проект на собственный диск в новом каталоге
  - Создать виртуальное окружение
  - Установить зависимости командой:
```python
pip install -r requirements.txt
```
<details>
<summary>Прописать переменные окружения в файле `.env.sample`</summary>
   
```dotenv
SECRET_KEY='Секретный ключ Django'
DEBUG='True/False', например: True

POSTGRES_DB_NAME='Название базы данных', например: 'name_of_db' или 'django_ticket'
POSTGRES_DB_USER='Пользователь базы данных', например: 'db_user' или 'postgres'
POSTGRES_DB_PASSWORD='Пароль пользователя базы данных', например: 'your_password'
POSTGRES_DB_HOST='Хост базы данных', например: '127.0.0.1' или 'localhost' или 'db' для Docker
POSTGRES_DB_PORT='Порт базы данных', например: '5432'

# Superuser
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=admin

# Celery
CELERY_BROKER_URL=redis://127.0.0.1:6379/0
CELERY_RESULT_BACKEND=redis://127.0.0.1:6379/0
CELERY_TIMEZONE=Europe/Moscow
```
</details>

<details>
<summary>Создать базу данных (в данном проекте используется PostgreSQL)</summary>

```python
psql -U postgres
create database django_ticket;
\q
```
</details>

- Применить миграции командой:
    ```python
    python manage.py migrate
    ```

<details>
<summary>Для создания тестового пользователя - администратор:</summary>

- login: admin@example.com
- password: admin 
    ```python
    python manage.py csu
    ```
</details>

<details>
<summary>Для заполнения базы данными:</summary>

```python
python manage.py fill_db
```
</details>
 
<details>
<summary>Для запуска сервера через терминал:</summary>

- Запустить Apache Kafka (zookeeper-server) (в окне терминала под Ubuntu)
    ```linux
    bin/zookeeper-server-start.sh config/zookeeper.properties
    ```
- Запустить Apache Kafka (kafka-server) (в окне терминала под Ubuntu)
    ```linux
    bin/kafka-server-start.sh config/server.properties
    ```
- Запустить Redis (в окне терминала под Ubuntu)
    ```linux
    sudo service redis-server start
    ```
- Запустить celery (в другом окне терминала)
    ```python
    celery -A config worker -l INFO -P eventlet
    ```
- Запустить tasks (в другом окне терминала)
    ```python
    celery -A config beat -l info -S django
    ```
- Запустить сервер (в другом окне терминала)
    ```python
    python manage.py runserver
    ```
- Запустить Apache Kafka - Consumer (в другом окне терминала)
    ```python
    python manage.py consumer
    ```
</details>

</details>

***

### Для завершения работы необходимо:

 - Нажать комбинацию клавиш `CTRL + C` в каждом окне терминала
 - Остановить Redis командой: sudo service redis-server stop

***

<details>
<summary><b>Connect with me:</b></summary>
   <p align="left">
       <a href="mailto:platonovpochta@gmail.com"><img src="https://img.shields.io/badge/gmail-%23EA4335.svg?style=plastic&logo=gmail&logoColor=white" alt="Gmail"/></a>
       <a href="https://wa.me/79217853835"><img src="https://img.shields.io/badge/whatsapp-%2325D366.svg?style=plastic&logo=whatsapp&logoColor=white" alt="Whatsapp"/></a>
       <a href="https://t.me/platonov_sm"><img src="https://img.shields.io/badge/telegram-blue?style=plastic&logo=telegram&logoColor=white" alt="Telegram"/></a>
   </p>
</details>
