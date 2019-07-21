________________________________________________________________

ЗАПУСК
________________________________________________________________

Terminal 1:
-Запуск gulp
gulp

Terminal 2:
-Запуск локального сервера
cd env/Scripts
activate.bat
cd ..
cd ..
py manage.py runserver


________________________________________________________________

УСТАНОВКА
________________________________________________________________

-Создание и запуск виртуального окружения
py -m venv env
cd env/Scripts
activate.bat
cd ..
cd ..

-Устнаовка плагинов
pip install django django-livereload-server psycopg2

-Скачать nodejs

-Инициализация
npm init  		# создание package.json

-Установка
npm i -g gulp bower eslint

-Сохранение в package.json
npm i gulp --save-dev	        # создание node_modules

-Сохранение в package.json плагинов
npm i gulp-sass gulp-concat gulp-clean-css gulp-rename gulp-autoprefixer gulp-notify gulp-livereload --save-dev

-Скачать git

-Скачивание библиотек
bower i jquery


________________________________________________________________

ДОПОЛНИТЕЛЬНО
________________________________________________________________

-Команды Django
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py dumpdata > dump.json
py manage.py loaddata dump.json

-Создать requirements.txt
pip freeze > requirements.txt

-Установить пакеты из requirements.txt
pip install -r requirements.txt

-Установка сетки
npm i smart-grid --save-dev
-Создать smart-grid-config.js
node smart-grid-config.js

-Проверить версию
npm -v
gulp -v