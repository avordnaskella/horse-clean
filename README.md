# Конный спорт — веб-приложение на Django

Проект представляет собой полнофункциональное веб-приложение для каталога дисциплин конного спорта. Реализованы CRUD-операции, динамическая фильтрация, адаптивный дизайн, интерактивные элементы (анимированная лошадь, игра «Корида») и видео-страница.


Сайт доступен по адресу:  
https://horse-clean.onrender.com/ 

Бесплатный хостинг (Render) может иметь задержку при первом открытии (до 50 секунд).


## Технологии
Backend - Django 6.0, Python 3.11  
 
Frontend - HTML, CSS, JavaScript  

База данных - PostgreSQL (Aiven)  
   
Хранение картинок - Cloudinary  
 
Деплой - Docker, Render  
 
Анимация - CSS, мемоизация


## Структура проекта
├── first_project/ # Настройки Django  
│ ├── settings.py  
│ ├── urls.py  
│ └── wsgi.py  
├── module_project/ # Основное приложение  
│ ├── models.py # Модели Category, Discipline  
│ ├── views.py # Представления (CRUD, AJAX)  
│ ├── forms.py # Формы с валидацией  
│ ├── admin.py # Регистрация моделей в админке  
│ ├── urls.py # Маршруты приложения  
│ └── templates/ # HTML-шаблоны  
├── static/ # Статические файлы  
│ ├── style.css # Стили (адаптив)  
│ ├── script.js # JS (фильтрация, модальное окно)  
│ ├── images/ # Картинки (лошадь, бык, коррида)  
│ └── videos/ # Видео об испанской школе  
├── media/ # Загружаемые картинки (через Cloudinary)  
├── Dockerfile # Инструкция для сборки образа  
├── requirements.txt # Зависимости Python  
└── README.md 

## Запуск
git clone https://github.com/avordnaskella/horse-clean.git  

python -m venv venv  

venv\Scripts\activate  
 
pip install -r requirements.txt  

python manage.py migrate  

(можно создать суперпользователя)  

python manage.py runserver

