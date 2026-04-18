FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt gunicorn whitenoise psycopg2-binary

COPY . .

# Выполняем миграции и собираем статику при запуске
CMD ["sh", "-c", "python manage.py migrate && echo 'from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(\"avordnaskella\", \"avordnaskella@gmail.com\", \"Arina*Piar2007\") if not User.objects.filter(username=\"avordnaskella\").exists() else None' | python manage.py shell && python manage.py runserver 0.0.0.0:8000"]
