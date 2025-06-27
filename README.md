# Foodgram
Проект выполнил Почекунин Алексей.
## Описание проекта
Foodgram - это проект, который дает возможность пользователям создавать и хранить рецепты на онлайн-платформе. Кроме того, есть возможность скачать список продуктов, необходимых для приготовления блюда, посмотреть рецепты друзей и добавить любимые рецепты в список избранных.
Чтобы использовать все возможности сайта — нужна регистрация. Проверка адреса электронной почты не осуществляется, вы можете ввести любой email. Заходите и делитесь своими любимыми рецептами!
## Технологии
1) Python
2) Django
3) Django REST Framework
4) SimpleJWT
5) Djoser
## Запуск проекта локально

Склонируйте репозиторий себе на компьютер и перейдите в папку backend:
``` bash
git clone https://github.com/dableshevich/foodgram-st.git
cd foodgram-st/backend/
```

Выполните миграции:
``` BASH
python manage.py migrate
```
Создайте администратора:
``` BASH
python manage.py createsuperuser
```

### Загрузите в базу данных собранные зарание данные
В проекте имеются файлы для начального заполнения базы данных, на ваш выбор выполните одну из следующих команд:
1) Загрузить тестовые данные( пользователи, рецепты и ингредиенты):
``` BASH
python manage.py loaddata collected_data.json
```
2) Загрузить только список ингредиентов:
``` BASH
python manage.py load_ingredients
```
---
Теперь можно запускать проект:
``` BASH
python manage.py runserver
```
## Полный запуск проекта
1) Для полного запуска сайта вам необходимо установить Docker.
   
2) Далее склонируйте репозиторий себе на компьютер и перейдите в корневую папку проекта:
``` bash
git clone https://github.com/dableshevich/foodgram-st.git
cd foodgram-st/
```

3) В корневой папке вам нужно создать `.env` файл (в директории лежит `.env.example` файл, для примера)
``` python
DB_ENGINE=django.db.backends.postgres # Data Base
POSTGRES_USER=postgres # Username of database owner
POSTGRES_PASSWORD=postgres # Password of database owner
POSTGRES_DB=postgres # Name of database
DB_HOST=postgres # Name of docker postgres container
DB_PORT=5432 # Port of database (default=5432)
DJANGO_SECRET_KEY="..." # Your secret key
```

4) Перейдите в папку с инфраструктурой и выполните сборку проекта с помощью docker-compose
``` bash
cd infra/
sudo docker compose up --build
```

5) Откройте в текущей директории ещё один терминал и выполните в нём следующие команды:
- Выполнение миграций
``` bash
sudo docker compose exec backend python3 manage.py migrate
```
- Заполнение базы данных (выберите одно из двух)
    - Полный набор тестовых данных:
    ``` BASH
    sudo docker compose exec backend python3 manage.py loaddata collected_data.json              
    ```
    - Только список ингредиентов:
    ``` BASH
    sudo docker compose exec backend python3 manage.py load_ingredients
    ```

- Соберите статические файлы backend'а и скопируйте их в директорию `/collected_static/statis/`
``` BASH
sudo docker compose exec backend python3 manage.py collectstatic
```
``` BASH
sudo docker compose exec backend cp -r static/. /collected_static/static/
```
---
Сайт доступен через localhost или через 127.0.0.1
