Проект на фреймворке Django

Выгрузите репозиторий командой git clone https://github.com/Alena1122001/project_golshop

В этом репозитории отсутствует виртуальное окружение, поставьте его командой python -m venv venv

активируйте venv, если он не активировался автоматически

venv\Scripts\activate.bat или venv\Scripts\activate.bat

Установите psycopg2, Pillow, django, django-debug-toolbar

Внесите изменение в settings для БД (DATABASES)

Выполнить миграцию БД: python manage.py makemigrations python manage.py migrate

Запустить скрипты переноса данных в БД

Запустите проект командой python manage.py runserver (или Ctrl+F5 для Visual Studio)

Перейдите по адресу http://127.0.0.1:8000 - стартовая страница
