﻿﻿________________________________________________________________

ЗАПУСК
________________________________________________________________

Terminal 1:  
-Запуск gulp  
gulp

Terminal 2:  
-Запуск локального сервера  
cd set_fullstackenv/Scripts  
activate.bat  
cd ..  
cd ..  
py devmanage.py runserver


________________________________________________________________

УСТАНОВКА
________________________________________________________________

-Создание и запуск виртуального окружения:  
py -m venv set_fullstackenv  
cd set_fullstackenv/Scripts  
activate.bat  
cd ..  
cd ..

-Устнаовка плагинов:  
pip install django django-livereload-server psycopg2 django-analytical

-Скачать nodejs

-Инициализация:  
npm init  		# создание package.json

-Установка:  
npm i -g gulp bower eslint

-Сохранение в package.json:  
npm i gulp --save-dev	        # создание node_modules

-Сохранение в package.json плагинов:  
npm i gulp-sass gulp-concat gulp-uglify-es gulp-clean-css gulp-rename gulp-autoprefixer gulp-notify gulp-livereload --save-dev

-Скачать git

-Скачивание библиотек:  
bower i jquery bootstrap components-font-awesome --save


________________________________________________________________

ДОПОЛНИТЕЛЬНО
________________________________________________________________

-Команды Django:  
py devmanage.py makemigrations
py devmanage.py migrate
py devmanage.py createsuperuser  
py devmanage.py dumpdata > dump.json  
py devmanage.py loaddata dump.json

-Создать requirements.txt:  
pip freeze > requirements.txt

-Установить пакеты из requirements.txt:  
pip install -r requirements.txt

-Установка сетки:  
npm i smart-grid --save-dev  
-Создать smart-grid-config.js  
node smart-grid-config.js

-Проверить версию:  
npm -v  
gulp -v
